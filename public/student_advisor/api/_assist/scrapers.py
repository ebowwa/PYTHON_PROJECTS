import asyncio
from api._assist .async_scraper import AsyncScraper
from api._assist.foundation import (
    fetch_institution_agreements,
    fetch_agreements_categories,
    fetch_agreements,
    fetch_articulation_agreements,
    get_agreements,
    get_keys,
    get_pdfs
)

class AssistOrgAPI:
    def __init__(self, school_id, major, major_code, delay=1):
        self.school_id = school_id
        self.major = major
        self.major_code = major_code
        self.delay = delay
        self.scraper = AsyncScraper()

    async def fetch_institution_agreements(self, institution_id):
        return await fetch_institution_agreements(self.scraper, institution_id)

    async def fetch_agreements_categories(self, receiving_institution_id, sending_institution_id, academic_year_id):
        return await fetch_agreements_categories(self.scraper, receiving_institution_id, sending_institution_id, academic_year_id)

    async def fetch_agreements(self, receiving_institution_id, sending_institution_id, academic_year_id, category_code):
        return await fetch_agreements(self.scraper, receiving_institution_id, sending_institution_id, academic_year_id, category_code)

    async def fetch_articulation_agreements(self, key):
        return await fetch_articulation_agreements(self.scraper, key)

    async def get_agreements(self):
        return await get_agreements(self.scraper, self.school_id, self.major)

    async def get_keys(self):
        return await get_keys(self.scraper, self.school_id, self.major, self.delay)

    async def get_pdfs(self):
        keys = await self.get_keys()
        return await get_pdfs(self.scraper, self.school_id, self.major_code, keys, self.delay)
