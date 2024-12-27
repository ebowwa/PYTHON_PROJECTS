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
