import argparse, json

from langchain_community.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

from get_embedding_function import get_embedding_function
import pprint

CHROMA_PATH = "chroma"

# PROMPT_TEMPLATE = """
# Answer the question based only on the following context:

# {context}

# ---

# Answer the question based on the above context: {question}
# """

def main():
    # read chroma database ids
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=get_embedding_function())
    # get all the ids
    ids = db.get(include=[])["ids"]
    print(type(ids))
    
    # for k, id in zip(range(10), ids):
    #     print(k, id)
    
    # I want to print all the ids with its index
    for k, id in enumerate(ids):
        print(k, id)
    
    # data = json.loads(ids)
# print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# print(data['name'])  # Output: John
# print(json_string)

    # for key, value in data.items():
    #     print(key, value)

    # print(list(ids[0]))

    # print(ids)    
    # save the ids to a file
    with open("db_ids_list.txt", "w") as f:
        for k, id in enumerate(ids):
            print(k, id)
            f.write(f"{k} - {id}\n")
    
    
if __name__ == "__main__":
    main()
