import requests

def scrape_endpoint(url, headers=None):
    """
    Generic function to scrape data from a given URL.
    """
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def fetch_institution_agreements(institution_id):
    return scrape_endpoint(f"https://assist.org/api/institutions/{institution_id}/agreements")

def fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id):
    return scrape_endpoint(f"https://assist.org/api/agreements/categories?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}")

def fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code):
    return scrape_endpoint(f"https://assist.org/api/agreements?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}&categoryCode={category_code}")

def fetch_articulation_agreements(key):
    return scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")
