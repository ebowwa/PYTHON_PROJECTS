
import requests

def list_indexes(api_url, headers):
    url = f"{api_url}/indexes?page=1&page_limit=10&sort_by=created_at&sort_option=desc"
    response = requests.get(url, headers=headers)
    return response.json()
