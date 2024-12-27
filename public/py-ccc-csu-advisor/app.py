from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn
from scrapers import AsyncScraper, InstitutionFetcher, AssistOrgAPI
from models import AgreementQuery  # Import the AgreementQuery class from models.py

# Assuming the classes AsyncScraper, InstitutionFetcher, and AssistOrgAPI are defined as provided in your script

app = FastAPI()


@app.get("/institutions", response_model=list)
async def get_institutions():
    try:
        fetcher = InstitutionFetcher()
        institutions = await fetcher.fetch_institutions()
        return institutions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/institution-agreements/{institution_id}", response_model=list)
async def get_institution_agreements(institution_id: int):
    try:
        api = AssistOrgAPI(school_id=institution_id, major="", major_code="")
        agreements = await api.fetch_institution_agreements(institution_id)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agreements-categories/")
async def get_agreements_categories(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        categories = await api.fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id)
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agreements/")
async def get_agreements(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int, category_code: str):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        agreements = await api.fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/articulation-agreements/{key}", response_model=dict)
async def get_articulation_agreements(key: str):
    try:
        scraper = AsyncScraper()
        agreement = await scraper.scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")
        return agreement
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query-agreements/")
async def query_agreements(query: AgreementQuery):
    try:
        api = AssistOrgAPI(school_id=query.receiving_institution_id, major="", major_code="")
        if query.category_code:
            agreements = await api.fetch_agreements(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id, query.category_code)
        else:
            agreements = await api.fetch_agreements_categories(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



# To run the server, use the following command in your terminal:
# uvicorn app:app --reload
