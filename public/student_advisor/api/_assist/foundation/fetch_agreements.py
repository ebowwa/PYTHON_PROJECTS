
async def fetch_agreements(scraper, receiving_institution_id, sending_institution_id, academic_year_id, category_code):
    return await scraper.scrape_endpoint(f"https://assist.org/api/agreements?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}&categoryCode={category_code}")
