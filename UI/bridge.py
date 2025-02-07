import random
import requests
import time


def get_llm_response(prompt: str):
    # time.sleep(10)
    url = f'http://localhost:5001/ai'  # URL of the 'ai' app
   
    print(f"{prompt}")   
    
    
    response = requests.post(url, json={"Prompt": prompt})    
    answer = response.json()
   
    # answer_pythondict = answer["Response"]
    # sources_python = answer["Sources"]
    # print(answer_pythondict, sources_python)
    
    # return answer
    # return answer["Response"], answer["Sources"]
    return answer


def get_response():
     # Catch the exception and retry a few times.   
    max_retry = 5
    for i in range(max_retry):
        try:
            response = requests.get(
                "http://app.athenalabo.com/api/thread/pending",
                headers={"X-API-KEY": "secret"},
            )
            response.raise_for_status()

            return response
        except Exception as e:
            if i == max_retry - 1:
                raise e
            else:
                print(f"Error {e} while trying to get pending threads. Retrying...")

def main(): 
    interval = 5
    while True:
        reply = get_response()

        threads = reply.json()
        if threads is None:
            print("No threads pending...")
            time.sleep(interval)

            continue

        print(f"Answering {len(threads)}...")

        for thread in threads:
            print(f"Answering thread {thread['id']}...")

            response = requests.get(
                f"http://app.athenalabo.com/api/thread/{thread['id']}/prompt/messages",
                headers={"X-API-KEY": "secret"},
            )
            response.raise_for_status()

            messages = response.json()["messages"]
            answer = get_llm_response(messages[-1]["content"])

                     
            response = requests.post(
                f"http://app.athenalabo.com/api/thread/{thread['id']}/prompt/answer",
                json={"content": answer["Response"],
                     },
                headers={"X-API-KEY": "secret"},
            )
            
            
            
            response.raise_for_status()

        time.sleep(interval)
        

if __name__ == '__main__':
    main()