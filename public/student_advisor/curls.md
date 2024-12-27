For the provided FastAPI script, I will create a series of curl commands to interact with each of the API endpoints. These commands are designed to demonstrate how you could make requests to each endpoint from the command line. Note that for endpoints requiring path or query parameters, you should replace the placeholders with actual values.

### 1. Get Institutions
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/institutions' \
  -H 'accept: application/json'
```

### 2. Get Institution Agreements
Replace `{institution_id}` with the actual institution ID.
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/institution-agreements/{institution_id}' \
  -H 'accept: application/json'
```

### 3. Get Agreements Categories
Replace placeholders with actual values for `receiving_institution_id`, `sending_institution_id`, and `academic_year_id`.
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/agreements-categories/?receiving_institution_id={receiving_institution_id}&sending_institution_id={sending_institution_id}&academic_year_id={academic_year_id}' \
  -H 'accept: application/json'
```

### 4. Get Agreements
Replace placeholders with actual values for `receiving_institution_id`, `sending_institution_id`, `academic_year_id`, and `category_code`.
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/agreements/?receiving_institution_id={receiving_institution_id}&sending_institution_id={sending_institution_id}&academic_year_id={academic_year_id}&category_code={category_code}' \
  -H 'accept: application/json'
```

### 5. Get Articulation Agreements
Replace `{key}` with the actual key.
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/articulation-agreements/{key}' \
  -H 'accept: application/json'
```

### 6. Query Agreements
This endpoint requires a POST request with a JSON body. You'll need to replace the JSON example with actual query parameters.
```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/api/query-agreements/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "receiving_institution_id": 1,
  "sending_institution_id": 2,
  "academic_year_id": 2023,
  "category_code": "EXAMPLE_CODE"
}'
```

### 7. Custom OpenAPI
```sh
curl -X 'GET' \
  'http://127.0.0.1:8000/api/openapi' \
  -H 'accept: application/json'
```

Ensure that your FastAPI application is running on `localhost` (127.0.0.1) on port 8000. If your application is hosted on a different address or port, adjust the URLs in the curl commands accordingly. Also, replace placeholder values with actual data where necessary.