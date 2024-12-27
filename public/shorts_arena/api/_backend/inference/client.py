import openai

# OpenAI client class
class OpenAIClient:
    def __init__(self, api_key, base_url):
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )

    def get_chat_response(self, message):
        response = self.client.chat.completions.create(model="ollama/mistral", messages=[
            {
                "role": "user",
                "content": message
            }
        ])
        return response

if __name__ == "__main__":
    # Example usage
    client = OpenAIClient(api_key="null", base_url="https://dev-hub.agentartificial.com")
    response = client.get_chat_response("you are a short clip narrator. you respond in a style that starts and ends in a loop. you attract.. rather manipulatively attract viewers attention. you do not reply in short form")
    print(response)