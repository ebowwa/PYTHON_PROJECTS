
async def fetch_institution_agreements(scraper, institution_id):
    return await scraper.scrape_endpoint(f"https://assist.org/api/institutions/{institution_id}/agreements")
