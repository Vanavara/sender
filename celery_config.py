# thirdparty
import sentry_sdk
from celery import Celery, signals
from kombu import Exchange, Queue
from sentry_sdk.integrations.celery import CeleryIntegration

# project
import settings

app = Celery(
    "recurrent_tasks",
    broker=settings.CELERY_BROKER_URL,
    backend="redis://{host}:{port}/0".format(host=settings.REDIS_HOST, port=settings.REDIS_PORT),
    include=["recurrent_tasks"],
)


@signals.celeryd_init.connect
def init_sentry(**_kwargs):
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        integrations=[
            CeleryIntegration(monitor_beat_tasks=True, propagate_traces=True),
        ],
    )


app.conf.task_routes = (
    [
        ("recurrent_tasks.*", {"queue": "tasks"}),
    ],
)

app.conf.worker_max_tasks_per_child = 1
app.conf.worker_concurrency = 1
app.conf.task_time_limit = 600
app.conf.worker_max_memory_per_child = 1024 * 1024 * 512

app.conf.result_expires = 3600

app.conf.task_queues = (Queue("tasks", Exchange("tasks", type="topic"), routing_key="recurrent_tasks.#"),)

app.conf.task_default_queue = "tasks"
