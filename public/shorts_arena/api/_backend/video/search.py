import requests

def search(api_url, headers, index_id, query, search_options):
    search_url = f"{api_url}/search"
    data = {
        "query": query,
        "index_id": index_id,
        "search_options": search_options,
    }
    response = requests.post(search_url, headers=headers, json=data)
    return response.json()
