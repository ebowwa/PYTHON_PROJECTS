import requests
import time
import pprint

# Prerequisites: Make sure these variables are defined
# INDEX_ID: unique identifier of your index
# VIDEO_URL: URL of the video to upload
# API_KEY: your API key for authentication
# API_URL: base URL of the API

# Declare the /tasks endpoint
TASKS_URL = f"{API_URL}/tasks"

# Prepare the request data
data = {
    "index_id": INDEX_ID,
    "language": "en",
    "video_url": VIDEO_URL,
}

# Upload the video
response = requests.post(TASKS_URL, headers={"x-api-key": API_KEY}, json=data)

# Extract and print the task ID and response
TASK_ID = response.json().get("_id")
print(f"Status code: {response.status_code}")
pprint.pprint(response.json())

# Optional: Monitor the indexing process
TASK_STATUS_URL = f"{API_URL}/tasks/{TASK_ID}"
while True:
    response = requests.get(TASK_STATUS_URL, headers={"x-api-key": API_KEY})
    STATUS = response.json().get("status")
    if STATUS == "ready":
        break
    time.sleep(10)

# Optional: Extract and print the video ID and response
VIDEO_ID = response.json().get('video_id')
print(f"Status code: {STATUS}")
print(f"VIDEO ID: {VIDEO_ID}")
pprint.pprint(response.json())