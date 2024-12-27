
from aiohttp import ClientResponseError
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import logging

from api._assist.institution_fetch import InstitutionFetcher
from api._assist.models import AgreementQuery, ArticulationAgreement
from api._assist.scrapers import AssistOrgAPI
from api._assist.async_scraper import AsyncScraper

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/api/institutions", response_model=list)
async def get_institutions():
    try:
        fetcher = InstitutionFetcher()
        institutions = await fetcher.fetch_institutions()
        return institutions if institutions else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/institution-agreements/{institution_id}", response_model=list)
async def get_institution_agreements(institution_id: int):
    try:
        api = AssistOrgAPI(school_id=institution_id, major="", major_code="")
        agreements = await api.fetch_institution_agreements(institution_id)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agreements-categories/")
async def get_agreements_categories(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        categories = await api.fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id)
        return categories
    except ClientResponseError as e:
        raise HTTPException(status_code=e.status, detail=f"Failed to retrieve agreement categories: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agreements/")
async def get_agreements(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int, category_code: str):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        agreements = await api.fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/articulation-agreements/{key}", response_model=ArticulationAgreement)
async def get_articulation_agreements(key: str) -> ArticulationAgreement:
    try:
        scraper = AsyncScraper()
        agreement_data = await scraper.scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")

        # Assuming agreement_data is a dict that matches the ArticulationAgreement model
        agreement = ArticulationAgreement.validate(agreement_data)
        return agreement
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query-agreements/")
async def query_agreements(query: AgreementQuery):
    try:
        # Now using major and major_code from the query object
        api = AssistOrgAPI(school_id=query.receiving_institution_id, major=query.major, major_code=query.major_code)

        if query.category_code:
            agreements = await api.fetch_agreements(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id, query.category_code)
        else:
            agreements = await api.fetch_agreements_categories(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id)

        return agreements
    except Exception as e:
        logger.error(f"Failed to fetch agreements: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error fetching agreements")


@app.get("/api/openapi", include_in_schema=False)
async def custom_openapi():
    return JSONResponse(content=app.openapi())


# To run the server, use the following command in your terminal:
# uvicorn app:app --reload # app.py
# uvicorn api.index:app --reload # api/index.py
