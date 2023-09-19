# stdlib
import os


# thirdparty
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]
DATABASE_URL_PSYCOPG2 = os.environ["DATABASE_URL_PSYCOPG2"]

API_TOKEN = os.environ["API_TOKEN"]

EXTERNAL_API=os.environ["EXTERNAL_API"]

RABBITMQ = {
    "PROTOCOL": "amqp",
    "HOST": os.getenv("RABBITMQ_HOST", "localhost"),
    "PORT": os.getenv("RABBITMQ_PORT", 5672),
    "USER": os.getenv("RABBITMQ_USER", "guest"),
    "PASSWORD": os.getenv("RABBITMQ_PASSWORD", "guest"),
}

CELERY_BROKER_URL = (
    f"{RABBITMQ['PROTOCOL']}://{RABBITMQ['USER']}:{RABBITMQ['PASSWORD']}@{RABBITMQ['HOST']}:{RABBITMQ['PORT']}"
)

SENTRY_DSN = os.environ["SENTRY_DSN"]

REDIS_HOST = os.environ["REDIS_HOST"]
REDIS_PORT = int(os.environ["REDIS_PORT"])

CRONTAB_OFFSET_IN_HOUR = int(os.environ["CRONTAB_OFFSET_IN_HOUR"])

