import asyncio
from httpx import AsyncClient

class AsyncScraper:
    """
    Handles asynchronous web scraping.
    """
    async def scrape_endpoint(self, url, headers=None):
        """
        Generic function to scrape data from a given URL asynchronously.
        """
        async with AsyncClient() as client:
            try:
                response = await client.get(url, headers=headers)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                raise Exception(f"Failed to fetch data: {str(e)}")

class InstitutionFetcher(AsyncScraper):
    """
    Fetches institution-related data using the AsyncScraper.
    """
    async def fetch_institutions(self):
        """
        Fetches a list of institutions from the assist.org API.
        """
        return await self.scrape_endpoint("https://assist.org/api/institutions")

class AssistOrgAPI:
    def __init__(self, school_id, major, major_code, delay=1):
        self.school_id = school_id
        self.major = major
        self.major_code = major_code
        self.delay = delay
        self.scraper = AsyncScraper()

    async def fetch_institution_agreements(self, institution_id):
        return await self.scraper.scrape_endpoint(f"https://assist.org/api/institutions/{institution_id}/agreements")

    async def fetch_agreements_categories(self, receiving_institution_id, sending_institution_id, academic_year_id):
        return await self.scraper.scrape_endpoint(f"https://assist.org/api/agreements/categories?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}")

    async def fetch_agreements(self, receiving_institution_id, sending_institution_id, academic_year_id, category_code):
        return await self.scraper.scrape_endpoint(f"https://assist.org/api/agreements?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}&categoryCode={category_code}")

    async def fetch_articulation_agreements(self, key):
        return await self.scraper.scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")

    async def get_agreements(self):
        data = await self.scraper.scrape_endpoint(f'https://assist.org/api/institutions/{self.school_id}/agreements')
        agreement_list = []
        for agreement in data:
            if agreement['isCommunityCollege']:
                school_id = agreement['institutionParentId']
                year = agreement['sendingYearIds'][-1]
                curr = {'id': school_id, 'year': year}
                agreement_list.append(curr)
        return agreement_list

    async def get_keys(self):
        agreement_list = await self.get_agreements()
        keys = []
        for agreement in agreement_list:
            await asyncio.sleep(self.delay)
            school_id, year = agreement['id'], agreement['year']
            data = await self.scraper.scrape_endpoint(f'https://assist.org/api/agreements?receivingInstitutionId={self.school_id}&sendingInstitutionId={school_id}&academicYearId={year}&categoryCode=major')
            data = data['reports']
            for report in data:
                if report['label'] == self.major:
                    keys.append({'key': report['key'], 'school_id': school_id})
        return keys

    async def get_pdfs(self):
        keys = await self.get_keys()
        id_to_key = {}
        for key in keys:
            key_val = key['key']
            school_id = key['school_id']
            id_to_key[school_id] = key_val
            pdf_url = f'https://assist.org/api/artifacts/{key_val}'
            async with AsyncClient() as client:
                response = await client.get(pdf_url)
                if response.status_code == 200:
                    file_name = f'agreements/report_{self.school_id}_{school_id}_{self.major_code}.pdf'
                    with open(file_name, 'wb') as f:
                        f.write(response.content)
                await asyncio.sleep(self.delay)
        return id_to_key
