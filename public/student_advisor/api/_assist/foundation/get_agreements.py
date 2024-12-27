
async def get_agreements(scraper, school_id, major):
    data = await scraper.scrape_endpoint(f'https://assist.org/api/institutions/{school_id}/agreements')
    agreement_list = []
    for agreement in data:
        if agreement['isCommunityCollege']:
            school_id = agreement['institutionParentId']
            year = agreement['sendingYearIds'][-1]
            curr = {'id': school_id, 'year': year}
            agreement_list.append(curr)
    return agreement_list
