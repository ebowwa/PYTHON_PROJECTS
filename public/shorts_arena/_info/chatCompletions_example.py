from openai import OpenAI

client = OpenAI(
    api_key="null",
    base_url="https://dev-hub.agentartificial.com",
)

response = client.chat.completions.create(model="ollama/mistral", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem about ducks wearing fedoras."
    }
])

print(response)