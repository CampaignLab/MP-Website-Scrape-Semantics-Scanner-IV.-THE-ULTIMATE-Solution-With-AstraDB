#!/usr/bin/env python3

# DISCLAIMER: The Application code scrpt and tool is intended to facilitate research, by authorised and approved parties, pursuant to the ideals of libertarian democracy in the UK, by Campaign Lab membership. Content subject-matter and results can be deemed sensitive and thus confidential. Therefore illicit and authorisation for any other use, outside these terms, is hereby not implied pursuant to requisite UK Data Protection legislation and the wider GDPR enactments within the EU.

# CODE REVISION: Ejimofor Nwoye, Newspeak House, London, England, @ 7th February 2025

import requests
from bs4 import BeautifulSoup
import re
import json
from langchain.embeddings import HuggingFaceEmbeddings
from cassio import AstraDB
from langchain.vectorstores import Cassandra
import os


os.system('clear')

# URLs to scrape
mp_list_url = "https://www.theyworkforyou.com/mps/"
constituencies_url = "https://members.parliament.uk/constituencies"

# Scrape MP profiles
def scrape_mps():
    response = requests.get(mp_list_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    mps = []
    for mp in soup.select(".people-list a"):  # Adjust selector as needed
        name = mp.get_text(strip=True)
        profile_url = "https://www.theyworkforyou.com" + mp["href"]
        
        # Extract statements from MP profile
        statements = extract_mp_statements(profile_url)
        
        mps.append({"name": name, "profile_url": profile_url, "statements": statements})
    
    return mps

# Extract policy interests and statements
def extract_mp_statements(profile_url):
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    
    # Regular expressions to find policy interests & views
    policies = re.findall(r'\b(IPP sentences|sentencing reform|justice system|public safety)\b', text, re.IGNORECASE)
    
    return list(set(policies))

# Save data to JSON
def save_to_json(data, filename="ukmpprofile.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# Vectorize and Store in AstraDB
def store_in_astra(data):
    astra_db = AstraDB()
    vectorstore = Cassandra(embedding=HuggingFaceEmbeddings(), session=astra_db.session, keyspace=astra_db.keyspace, table_name="mp_profiles")
    
    for mp in data:
        vectorstore.add_texts(texts=[mp["statements"]], metadatas=[{"name": mp["name"], "profile_url": mp["profile_url"]}])

if __name__ == "__main__":
    mp_data = scrape_mps()
    save_to_json(mp_data)
    store_in_astra(mp_data)
    print("Data scraped, stored in JSON, and embedded in AstraDB.")

