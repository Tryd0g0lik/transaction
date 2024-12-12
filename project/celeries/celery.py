"""Creating the celery app"""
from celery import Celery
from dotenv_ import REDIS_URL
# The SOURCE the TASKS for LIST
CELERY_TASK_LIST = [
    "project.celeries.celery_tasks",
]

def celery_init_app() -> Celery:
    celery_app = Celery(
        "first_myCelery",
        include=CELERY_TASK_LIST,
        broker=f"{REDIS_URL}"
    )
    celery_app.conf['CELERY_TASK_SERIALIZER'] = 'json'
    celery_app.conf['CELERY_ACCEPT_CONTENT'] = ['json']
    celery_app.autodiscover_tasks(CELERY_TASK_LIST)
    celery_app.set_default()
    return celery_app

