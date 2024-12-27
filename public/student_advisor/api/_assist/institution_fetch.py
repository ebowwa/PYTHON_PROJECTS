# institution_fetch.py
import asyncio
from api._assist.async_scraper import AsyncScraper  

class InstitutionFetcher(AsyncScraper):
    """
    Fetches institution-related data using the AsyncScraper.
    """
    async def fetch_institutions(self):
        """
        Fetches a list of institutions from the assist.org API.
        """
        return await self.scrape_endpoint("https://assist.org/api/institutions")
