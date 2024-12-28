import argparse
from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function
import pprint

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    # read chroma database ids
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    # get all the ids
    ids = db.get(include=[])["ids"]

    print(ids)    
    # save the ids to a file
    with open("db_ids.txt", "w") as f:
        for id in ids:
            f.write(f"{id}\n")
    
    # Create CLI.
    # parser = argparse.ArgumentParser()
    # parser.add_argument("query_text", type=str, help="The query text.")
    # args = parser.parse_args()
    # query_text = args.query_text
    # query_rag(query_text)


if __name__ == "__main__":
    main()
