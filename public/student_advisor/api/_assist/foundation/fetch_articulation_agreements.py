
async def fetch_articulation_agreements(scraper, key):
    return await scraper.scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")
