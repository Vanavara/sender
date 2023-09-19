# thirdparty
from celery import Celery
import requests
import os

API_TOKEN = os.environ.get("API_TOKEN")
app = Celery('tasks', broker='CELERY_BROKER_URL')

@app.task(
    name="tasks.interact_with_external_api",
    autoretry_for=(requests.exceptions.ConnectionError, Exception),
    retry_backoff=30,
    max_retries=100,
    retry_jitter=False,
)
def interact_with_external_api():
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get("EXTERNAL_API", headers=headers)