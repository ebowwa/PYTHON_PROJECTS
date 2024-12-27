import requests

def exa_api_search(query):
    url = "https://api.exa.ai/search"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": "aca455e1-406e-45b2-8d3c-6cad1fd5fc5b"
    }

    # Adding a basic query to the payload
    payload = {"query": query}

    response = requests.post(url, json=payload, headers=headers)
    return response.text

if __name__ == '__main__':
    # Test the function with a sample query
    result = exa_api_search("youtube latest technology trends")
    print(result)