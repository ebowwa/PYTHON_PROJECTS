import requests
import json

def fetch_data(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data from {url}. Status code: {response.status_code}")
        return None

def print_institutions(data):
    print("\nInstitutions:")
    for institution in data:
        print(f"ID: {institution['id']}, Name: {institution['names'][0]['name']}")

def print_institution_agreements(data):
    print("\nInstitution Agreements:")
    for agreement in data:
        print(f"Institution Parent ID: {agreement['institutionParentId']}, "
              f"Institution Name: {agreement['institutionName']}, "
              f"Code: {agreement['code']}, "
              f"Is Community College: {agreement['isCommunityCollege']}")

def main():
    api_url = "http://127.0.0.1:8000/api"

    # Fetch institutions
    headers = {'accept': 'application/json'}
    institutions_data = fetch_data(f"{api_url}/institutions", headers)

    if institutions_data:
        print_institutions(institutions_data)

    # Fetch institution agreements
    institution_id = 97
    institution_agreements_data = fetch_data(f"{api_url}/institution-agreements/{institution_id}", headers)

    if institution_agreements_data:
        print_institution_agreements(institution_agreements_data)

if __name__ == "__main__":
    main()