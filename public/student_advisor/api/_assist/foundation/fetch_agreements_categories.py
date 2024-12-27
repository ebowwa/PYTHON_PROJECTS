
async def fetch_agreements_categories(scraper, receiving_institution_id, sending_institution_id, academic_year_id):
    return await scraper.scrape_endpoint(f"https://assist.org/api/agreements/categories?receivingInstitutionId={receiving_institution_id}&sendingInstitutionId={sending_institution_id}&academicYearId={academic_year_id}")
