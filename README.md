# MP-Website-Scrape-Semantics-Scanner-IV.-THE-ULTIMATE-Solution-With-AstraDB
This solution employs a Vector database for GenAI LLMs', Vector Search and RAG flows

DISCLAIMER: The Application code script and tool is intended to facilitate research, by authorised and approved parties, pursuant to the ideals of libertarian democracy in the UK, by Campaign Lab membership. Content subject-matter and results can be deemed sensitive and thus confidential. Therefore illicit and authorisation for any other use, outside these terms, is hereby not implied pursuant to requisite UK Data Protection legislation and the wider GDPR enactments within the EU.

AstraDB is built on top of the popular Apache Cassandra non-SQL database. DataStax provides AstraDB, as a multitenanted Database-As-A-Service (DaaS) offering in a multicloud environment. To signup for a free user account, follow the link: https://www.datastax.com/products/datastax-astra 

The Python code script is formatted for use on UNIX/LINUX and MacOS platforms and can be executed thus: [user]$ chmod u+x ukmpprofile_astradb.py 

The challenge and task requires web scraping, natural language processing (NLP) for extracting key political statements using Regular Expressions, and storing the data in Astra DB as vectors for retrieval-augmented generation (RAG). Here’s a breakdown of the approach:

Scraping Data: Using requests and BeautifulSoup to extract MP information from the given URLs.
Extracting Key Phrases: Using Regular Expressions (re module) to find political statements and views.
Storing Results: Saving the extracted data as ukmpprofile.json.
Embedding & Vectorization: Using langflow, cassio, and sentence_transformers to store and retrieve data from Astra DB for RAG.

This script scrapes MP profile pages, extracts political statements using regex, saves the data as JSON, and embeds it in Astra DB using LangChain and Cassio.


