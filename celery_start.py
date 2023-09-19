# stdlib
import logging

# thirdparty
from celery.schedules import crontab

# project
import settings
from celery_config import app

app.conf.beat_schedule = {
    # at 5 AM Moscow time (UTC+3)
    "check_and_start_broadcasts_task": {
        "task": "your_project.tasks.check_and_start_broadcasts",
        "schedule": crontab(minute=0, hour=settings.CRONTAB_OFFSET_IN_HOUR),
    },
}

app.conf.timezone = "UTC"
app.conf.task_acks_late = True
app.conf.beat_enabled = True


if __name__ == "__main__":
    # clear all stuck tasks
    app.control.purge()

    worker = app.Worker(
        include=[
            "check_and_start_broadcasts_task",
        ],
        queue="tasks",
        pool="prefork",
        beat=True,
        without_gossip=True,
    )

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    worker.start()
