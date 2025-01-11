## env
Use flask env for UI and gpu env for querydata.py and populate_database.py

# It ingest PDF and md files - last version 4.Jan.2025

# please use docling to convert any file format into md

# Reference rag-tutorial-v2
https://www.youtube.com/watch?v=2TJxpyO3ei4&t=847s
https://github.com/pixegami/rag-tutorial-v2






### Uses Ollmaa embedding model
## Both sources and query must use the same embedding model
## id of embedding files in chromadb to secure that later additional files can be added. Otherwise chroma creates own UUID

### PDF loader


##### populate_database.py (lines 15-28) Explanation:

This code is the main function that handles populating a database with document data. Let me break it down in simple terms.

The code first sets up a way for users to control how the program runs using command-line arguments. It creates a "--reset" flag option that users can include when running the program. When someone runs the program with this flag, it will clear out the existing database before adding new data.

For inputs, the code accepts command-line arguments (specifically checking for the --reset flag) and presumably works with documents that are loaded through the load_documents() function.

The outputs are changes to a database - either clearing it and/or adding new document data to it.

The code achieves its purpose through three main steps:

It loads documents using load_documents()
It splits these documents into smaller chunks using split_documents()
It adds these chunks to a database system called Chroma using add_to_chroma()
The logic flow is straightforward:

First, check if the user wants to reset the database
If yes, clear the database
Then, regardless of whether the database was cleared, load and process the documents
Finally, store the processed document chunks in the database
This code serves as the main orchestrator for a document processing pipeline, taking raw documents and preparing them for storage in a searchable database. While we don't see the implementation details of the helper functions it calls, we can understand that it's transforming documents into a format that can be effectively stored and retrieved later.
