import requests
import json

class ChatAssistant:
    def __init__(self, api_key, endpoint="https://api.openai.com/v1/chat/completions"):
        self.api_key = api_key
        self.endpoint = endpoint

    def generate_chat_completion(self, messages, model="gpt-4", temperature=1, max_tokens=None):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
        }

        if max_tokens is not None:
            data["max_tokens"] = max_tokens

        response = requests.post(self.endpoint, headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    API_KEY = "your_api_key_here"
    assistant = ChatAssistant(API_KEY)

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Anything you want to ask or know"}
    ]

    while True:
        response_text = assistant.generate_chat_completion(conversation)
        print("AI:", response_text)
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'stop']:
            break

        conversation.append({"role": "user", "content": user_input})
        conversation.append({"role": "system", "content": response_text})
