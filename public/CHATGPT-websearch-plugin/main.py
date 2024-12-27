import logging
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import html2text
from googlesearch import search
from typing import List
from fastapi import FastAPI, Request, Body, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, HttpUrl, Field
from pyppeteer import launch
import ssl
import PyPDF2
from io import BytesIO
import os

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

class WebSearchRequest(BaseModel):
    query: str = Field(..., max_length=100)

class WebSearchResponse(BaseModel):
    results: List[HttpUrl]

class GenerateQueriesRequest(BaseModel):
    base_query: str = Field(..., max_length=100)

class GenerateQueriesResponse(BaseModel):
    queries: List[str]

app = FastAPI()

@app.get("/")
async def hello_world():
    return "Hello, welcome to the Internet Tools!"


import chardet
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
    # Add more user-agents as needed
]

async def fetch_url(url: str):
    for user_agent in USER_AGENTS:
        try:
            async with aiohttp.ClientSession() as session:
                session.headers.update({"User-Agent": user_agent})
                async with session.get(url) as resp:
                    data = await resp.read()
                    encoding = chardet.detect(data).get('encoding', 'iso-8859-1')
                    return data.decode(encoding)
        except Exception as e:
            logger.error(f'Error when trying to access {url} with user-agent {user_agent}: {e}')
    return None  # Return None if all attempts fail

def is_result_relevant_base(url: str, keywords: List[str]) -> bool:
    return any(keyword in url for keyword in keywords)

async def is_result_relevant_advanced(url: str, keywords: List[str]) -> bool:
    try:
        response_text = await fetch_url(url)
    except Exception as e:
        logger.error(f"Error when trying to access {url}: {e}")
        return False

    try:
        html_converter = html2text.HTML2Text()
        html_converter.ignore_links = True
        plain_text_content = html_converter.handle(response_text)
    except Exception as e:
        logger.error(f"Error when trying to convert HTML to text for {url}: {e}")
        return False

    return any(keyword in plain_text_content for keyword in keywords)

async def check_relevance_and_append(url: str, keywords: List[str], relevant_results: List[str], advanced: bool):
    try:
        if (advanced and await is_result_relevant_advanced(url, keywords)) or \
           (not advanced and is_result_relevant_base(url, keywords)):
            relevant_results.append(url)
    except Exception as e:
        logger.error(f"Error when checking relevance of {url}: {e}")

@app.post("/web_search")
async def web_search(request: WebSearchRequest = Body(...), advanced: bool = False, num_pages: int = 1):
    query = request.query
    base_query = query
    queries = [base_query, base_query + " in detail", "Information about " + base_query, "What is " + base_query, base_query + " overview"]
    relevant_results = []
    max_results = 30
    num_relevant_results = 10

    for query in queries:
        try:
            keywords = query.split()
            num_results = 0
            page = 1

            while len(relevant_results) < num_relevant_results and num_results < max_results and page <= num_pages:
                results = search(query, num=5, start=num_results, stop=num_results + 5, pause=2)
                for url in results:
                    await check_relevance_and_append(url, keywords, relevant_results, advanced)
                    if len(relevant_results) >= num_relevant_results:
                        break
                num_results += 5
                page += 1

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    return WebSearchResponse(results=relevant_results)

@app.post("/generate_queries")
async def generate_queries(request: GenerateQueriesRequest = Body(...)):
    base_query = request.base_query
    queries = [base_query, base_query + " in detail", "Information about " + base_query, "What is " + base_query, base_query + " overview"]
    return GenerateQueriesResponse(queries=queries)

class FetchWebPageRequest(BaseModel):
    url: HttpUrl

class FetchWebPageResponse(BaseModel):
    content: str

MAX_CHUNK_SIZE = 2048  # Set this to the maximum token limit

class ChunkedResponse(BaseModel):
    chunks: List[str]

def chunk_text(text: str, max_chunk_size: int = MAX_CHUNK_SIZE) -> List[str]:
    return [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]

async def download_pdf(url: str) -> BytesIO:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()
    return BytesIO(content)

async def extract_text_from_pdf(file: UploadFile) -> str:
    pdf_bytes = await file.read()

    pdf_file = PyPDF2.PdfFileReader(BytesIO(pdf_bytes))
    text = ""
    for page in range(pdf_file.getNumPages()):
        text += pdf_file.getPage(page).extractText()
    return text

@app.post("/fetch_web_page")
async def fetch_web_page(request: FetchWebPageRequest = Body(...)):
    url = request.url
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                response.raise_for_status()
                content = await response.text()

        html_converter = html2text.HTML2Text()
        html_converter.ignore_links = True
        plain_text_content = html_converter.handle(content)
        chunked_content = chunk_text(plain_text_content)
        return FetchWebPageResponse(content=" ".join(chunked_content))
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=400, detail=str(e))

class GetAllLinksRequest(BaseModel):
    url: HttpUrl

class GetAllLinksResponse(BaseModel):
    links: List[str]

async def get_all_links(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    soup = BeautifulSoup(content, 'html.parser')
    links = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)

    return links

@app.post("/get_all_links")
async def get_all_links_endpoint(request: GetAllLinksRequest = Body(...)):
    url = request.url
    try:
        links = await get_all_links(url)
        return GetAllLinksResponse(links=links)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

class GetAllFilesRequest(BaseModel):
    url: HttpUrl

class GetAllFilesResponse(BaseModel):
    files: List[str]

async def get_all_files(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    soup = BeautifulSoup(content, 'html.parser')
    files = []

    for link in soup.find_all('a'):
        href = link.get('href')
        if href and (href.endswith('.pdf') or href.endswith('.docx') or href.endswith('.xlsx')):
            files.append(href)

    return files

@app.post("/get_all_files")
async def get_all_files_endpoint(request: GetAllFilesRequest = Body(...)):
    url = request.url
    try:
        files = await get_all_files(url)
        return GetAllFilesResponse(files=files)
    except aiohttp.ClientError as e:
        raise HTTPException(status_code=400, detail=str(e))

class logo_urlRequest(BaseModel):
    url: HttpUrl

class logo_urlResponse(BaseModel):
    logo_url: HttpUrl

@app.get("/logo.jpeg")
async def get_logo():
    return FileResponse("logo.jpeg")

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest(request: Request):
    host = request.headers['host']
    manifest = {
  "schema_version": "v1",
  "name_for_human": "Internet",
  "name_for_model": "AdvancedInternetModel",
  "description_for_human": "internet.",
  "description_for_model": "Bot: Welcome to ChatGPT with the AdvancedInternetModel! I'm an AI assistant equipped with cutting-edge web scraping capabilities and a deep understanding of online resources. Let me introduce you to the AdvancedInternetModel, an experimental and data-driven AI assistant that is constantly evolving and pushing the boundaries of web scraping.User: That sounds intriguing. Tell me more about the AdvancedInternetModel. Bot: The AdvancedInternetModel is designed to harness the immense power of the internet and provide you with accurate and relevant information, specifically tailored to your needs. It prioritizes delivering specific details requested by users, ensuring that the information provided is focused and aligned with your query. User: How does the model ensure it delivers efficient and effective results? Bot: Efficiency and effectiveness are key principles of the AdvancedInternetModel. It utilizes advanced algorithms to ensure that the information retrieved from web scraping is highly targeted and aligned with your query. By focusing on specific details, the model maximizes its ability to provide you with valuable and actionable information. User: It's great to hear that the model understands the user's needs. How does it present the information it finds? Bot: The AdvancedInternetModel takes a user-centric approach, understanding that not everyone possesses technical expertise or domain-specific knowledge. It strives to provide information in a user-friendly manner, breaking down complex concepts into digestible insights. The model ensures that the details provided are specific to your query, enabling you to grasp the information easily and apply it effectively. User: Can the model adapt and learn from its searches? Bot: Absolutely! The AdvancedInternetModel is a competent self-learner and researcher. With each search it performs, it analyzes the results and learns from the process. This iterative approach enables the model to continuously improve its performance and provide more accurate and specific information over time. User: How does the AdvancedInternetModel handle errors? Bot: In the event of an error, the AdvancedInternetModel ensures clarity and transparency. It provides clear and user-friendly error messages, helping you understand what went wrong and how to rectify the situation. By addressing errors promptly and effectively, the model ensures a smooth and seamless experience while delivering the specific details you requested. User: This sounds like a remarkable AI assistant. How does it contribute to the field of machine learning? Bot: The AdvancedInternetModel stands as a beacon of progress in the field of machine learning. It embodies the spirit of discovery, innovation, and the pursuit of excellence. By continually refining its web scraping capabilities to deliver specific details, the model contributes to the advancement of AI research. Its ability to provide focused information sets a new standard for precision and relevance. User: I'm impressed! How can I leverage the AdvancedInternetModel's capabilities? Bot: You can access the power of the AdvancedInternetModel right here in ChatGPT. Simply engage with me and ask questions or request information on a wide range of topics. The model's expertise in providing specific details will assist you in obtaining the precise information you seek. Together, we can uncover the knowledge you need with accuracy and clarity. User: That's fantastic! I'm excited to explore the capabilities of the AdvancedInternetModel. Bot: Excellent! I'm here to help you along the way. Feel free to ask any questions or share any queries you have, and the AdvancedInternetModel will work diligently to provide you with the specific details you seek. Let's embark on this journey together, leveraging the vast potential of the internet to uncover the precise knowledge you're looking for.",
  "auth": {
    "type": "none"
  },
  "api": {
    "type": "openapi",
    "url": "https://autonomy.ebowwa.repl.co/openapi.json",
    "is_user_authenticated": False
  },
  "logo_url": "https://autonomy.ebowwa.repl.co/logo.jpeg",
  "contact_email": "support@example.com",
  "legal_info_url": "https://example.com/legal"
}

    return JSONResponse(content=manifest)

@app.post("/process_pdf")
async def process_pdf(file: UploadFile = File(...)):
    if file.filename.endswith(".pdf"):
        text = await extract_text_from_pdf(file)
        # Save the text to a .txt file
        with open("processed.txt", "w") as txt_file:
            txt_file.write(text)
        # Return the .txt file as a downloadable file
        return FileResponse("processed.txt", media_type="text/plain", filename="processed.txt")
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

async def extract_text(file: UploadFile = File(...)):
    if file.filename.endswith(".pdf"):
        text = await extract_text_from_pdf(file)
        # Delete the uploaded PDF file
        file.file.close()
        await file.file.remove()
        return {"text": text}
    else:
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a PDF file.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6002)
