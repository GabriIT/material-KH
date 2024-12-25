import random
import requests
import time


def get_llm_response(prompt: str):
    # time.sleep(10)
    url = f'http://localhost:5001/ai'  # URL of the 'ai' app
   
    print(f"{prompt}")   
    
    
    response = requests.post(url, json={"Prompt": prompt})    
    answer = response.json()
    # return answer
    # return answer["Response"], answer["Sources"]
    return answer["Response"]




def main():
    # Initialize chatbot
    # chain = initialize_chatbot()

    while True:
        response = requests.get(
            "http://app.athenalabo.com/api/thread/pending",
            headers={"X-API-KEY": "secret"},
        )
        response.raise_for_status()

        threads = response.json()
        if threads is None:
            print("No threads pending...")
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
            # answer = ai_answer(messages[-1]["content"])

            answer = get_llm_response(messages[-1]["content"])
            print(answer)
            
            
            response = requests.post(
                f"http://app.athenalabo.com/api/thread/{thread['id']}/prompt/answer",
                json={"content": answer},
                headers={"X-API-KEY": "secret"},
            )
            response.raise_for_status()
            # print(response["content"])
        time.sleep(5)


if __name__ == '__main__':
    main()