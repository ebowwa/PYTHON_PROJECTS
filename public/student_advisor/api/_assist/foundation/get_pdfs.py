
async def get_pdfs(scraper, school_id, major_code, keys, delay):
    id_to_key = {}
    for key in keys:
        key_val = key['key']
        school_id = key['school_id']
        id_to_key[school_id] = key_val
        pdf_url = f'https://assist.org/api/artifacts/{key_val}'
        async with AsyncClient() as client:
            response = await client.get(pdf_url)
            if response.status_code == 200:
                file_name = f'agreements/report_{school_id}_{school_id}_{major_code}.pdf'
                with open(file_name, 'wb') as f:
                    f.write(response.content)
            await asyncio.sleep(delay)
    return id_to_key
