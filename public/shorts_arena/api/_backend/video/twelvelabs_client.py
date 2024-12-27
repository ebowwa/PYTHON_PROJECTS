
import os
from search import search
from auth import get_headers
from list_indexes import list_indexes

def exeTwelvelabs():
    headers = get_headers()
    API_URL = os.getenv("API_URL", "https://api.twelvelabs.io/v1.1")
    INDEX_ID = "<YOUR_INDEX_ID>"


    # Example of using list_indexes function
    indexes = list_indexes(API_URL, headers)
    print("Indexes:", indexes)

    # Example of using search function
    query = "car accidents"
    search_options = ["visual"]
    search_results = search(API_URL, headers, INDEX_ID, query, search_options)
    print("Search Results:", search_results)

if __name__ == "__main__":
  exeTwelvelabs()
