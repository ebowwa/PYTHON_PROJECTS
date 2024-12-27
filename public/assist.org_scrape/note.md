this is depreciated, but i didnt want to depart it yet, it works to scrape the assist.org site for students between ccc and csu transfer credits, it serves this as an api perfect to integrate into other tasks, functions, ui, workflows, etc

flask will be slower for this operation. fastapi was selected after pivot from flask, read these notes for reference:
```
Performance
FastAPI: It is designed to be fast. It's asynchronous and non-blocking and can handle large volumes of requests more efficiently than Flask. If performance under high load is a critical factor, FastAPI has an advantage.
Flask: It is a synchronous framework and might not perform as well as FastAPI in handling concurrent requests, especially I/O bound tasks like network requests.

For APIs involving heavy I/O operations (e.g., web scraping and serving data from those operations), FastAPI's asynchronous support can be particularly beneficial. It allows your application to make non-blocking calls to external APIs or databases, which is ideal for scraping and serving data.
```
