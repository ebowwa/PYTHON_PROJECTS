
async def get_keys(scraper, school_id, major, delay):
    agreement_list = await get_agreements(scraper, school_id, major)
    keys = []
    for agreement in agreement_list:
        await asyncio.sleep(delay)
        school_id, year = agreement['id'], agreement['year']
        data = await scraper.scrape_endpoint(f'https://assist.org/api/agreements?receivingInstitutionId={school_id}&sendingInstitutionId={school_id}&academicYearId={year}&categoryCode=major')
        data = data['reports']
        for report in data:
            if report['label'] == major:
                keys.append({'key': report['key'], 'school_id': school_id})
    return keys
