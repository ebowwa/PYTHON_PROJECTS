scrapers.py Documentation
Overview: This script is designed for asynchronous web scraping, particularly targeting data related to institutional agreements. It leverages modern asynchronous Python features for efficient data fetching.

Dependencies:

asyncio: For asynchronous programming support.
httpx: A fully featured HTTP client for Python 3, supporting asynchronous requests.
Classes:

AsyncScraper

Purpose: Provides a generic asynchronous web scraping utility.
Method: scrape_endpoint(self, url, headers=None)
Asynchronously fetches data from a specified URL.
Returns JSON data or raises an exception on failure.
InstitutionFetcher (inherits from AsyncScraper)

Purpose: Fetches a list of institutions asynchronously.
Method: fetch_institutions(self)
Uses scrape_endpoint to fetch institution data from the Assist.org API.
AssistOrgAPI

Purpose: Encapsulates API calls to Assist.org for retrieving institution agreements and related data.
Initialization Parameters: school_id, major, major_code, and delay for rate-limiting requests.
Methods:
fetch_institution_agreements(self, institution_id): Fetches agreements for a specific institution.
fetch_agreements_categories(self, receiving_institution_id, sending_institution_id, academic_year_id): Fetches agreement categories based on institutions and academic year.
fetch_agreements(self, receiving_institution_id, sending_institution_id, academic_year_id, category_code): Fetches detailed agreements based on criteria.
Additional methods for retrieving keys and PDFs related to agreements, demonstrating advanced scraping and asynchronous file handling.
Functionality:

The script showcases advanced asynchronous programming techniques, making it highly efficient for web scraping tasks.
It is specifically tailored to interact with the Assist.org API, focusing on the educational domain to fetch institutional agreement data.
Provides a structured approach to scraping, with error handling and rate-limiting features to comply with web service constraints.
app.py Documentation
Overview: This script utilizes FastAPI to create a web application that provides several endpoints related to institutional agreements. It integrates asynchronous operations, demonstrating advanced use of Python for web development.

Dependencies:

FastAPI: For creating web application endpoints.
HTTPException: For handling HTTP errors.
BaseModel: From Pydantic, for request body validation.
uvicorn: ASGI server for running the application.
Custom modules: scrapers.py and models.py for web scraping and data modeling.
Endpoints:

GET /institutions

Purpose: Fetches a list of institutions.
Response: List of institutions.
Implementation: Uses InstitutionFetcher from scrapers.py to asynchronously fetch institution data.
GET /institution-agreements/{institution_id}

Purpose: Fetches agreements for a specified institution.
Parameters: institution_id (int) - The ID of the institution.
Response: List of agreements for the given institution.
Implementation: Utilizes AssistOrgAPI from scrapers.py to fetch agreements.
GET /agreements-categories/

Purpose: Gets agreement categories based on institution IDs and academic year.
Parameters: receiving_institution_id, sending_institution_id, academic_year_id.
Response: Categories of agreements.
Implementation: Calls AssistOrgAPI.fetch_agreements_categories with the provided parameters.
GET /agreements/

Purpose: Fetches agreements based on detailed criteria.
Parameters: receiving_institution_id, sending_institution_id, academic_year_id, category_code.
Response: Agreements filtered by the provided criteria.
Implementation: AssistOrgAPI.fetch_agreements is called with the criteria.
GET /articulation-agreements/{key}

Purpose: Retrieves a specific articulation agreement.
Parameters: key (str) - A unique key identifying the agreement.
Response: Details of the specified articulation agreement.
Implementation: Uses AsyncScraper.scrape_endpoint to scrape data for a specific agreement.
POST /query-agreements/

Purpose: Queries agreements based on a set of criteria.
Request Body: An instance of AgreementQuery from models.py, containing query parameters.
Response: Agreements or categories based on the query.
Implementation: Conditional logic to fetch agreements or categories based on the presence of category_code.
Running the Application: The script includes a comment on using uvicorn to run the server with hot reload enabled for development purposes.

models.py Documentation
Overview: This script defines data models using Pydantic, which are utilized for validating and parsing data for the application's operations, particularly in handling requests.

Dependencies:

Pydantic: Utilized for data validation and settings management through Python data classes.
Optional: Imported from typing, used to denote optional fields within models.
Model Definitions:

AgreementQuery
Purpose: Represents query parameters for fetching agreements.
Fields:
receiving_institution_id: Integer, mandatory field representing the ID of the receiving institution.
sending_institution_id: Integer, mandatory field representing the ID of the sending institution.
academic_year_id: Integer, mandatory field representing the academic year ID.
category_code: String, optional field that, if provided, filters agreements by category.
This model is crucial for the application, as it defines the structure of request data for querying agreements, ensuring valid and correctly typed data is received for processing.

