import requests

class DataFetcher:
    def __init__(self, api_url):
        self.api_url = api_url
        self.headers = {'accept': 'application/json'}

    def fetch_data(self, endpoint):
        url = f"{self.api_url}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")
            return None

    @staticmethod
    def print_institutions(data):
        print("\nInstitutions:")
        for institution in data:
            print(f"ID: {institution['id']}, Name: {institution['names'][0]['name']}")

    @staticmethod
    def print_institution_agreements(data):
        print("\nInstitution Agreements:")
        for agreement in data:
            print(f"Institution Parent ID: {agreement['institutionParentId']}, "
                  f"Institution Name: {agreement['institutionName']}, "
                  f"Code: {agreement['code']}, "
                  f"Is Community College: {agreement['isCommunityCollege']}")

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api"
    data_fetcher = DataFetcher(api_url)

    # Fetch institutions
    institutions_data = data_fetcher.fetch_data("institutions")
    if institutions_data:
        DataFetcher.print_institutions(institutions_data)

    # Fetch institution agreements
    institution_id = 97
    institution_agreements_data = data_fetcher.fetch_data(f"institution-agreements/{institution_id}")
    if institution_agreements_data:
        DataFetcher.print_institution_agreements(institution_agreements_data)
