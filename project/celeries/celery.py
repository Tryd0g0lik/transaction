from celery import Celery
from flask import Flask
from dotenv_ import REDIS_URL
# The SOURCE the TASKS for LIST
CELERY_TASK_LIST = [
    "project,celeries.celery_tasks",
]

def celery_init_app(app: Flask) -> Celery:
    celery_app = Celery(
        app.import_name,
        include=CELERY_TASK_LIST,
        broker=f"{REDIS_URL}"
    )
    
    TaskBase = celery_app.Task
    class FlaskTask(TaskBase):
        def __call__(self, *args, **kwargs) -> object:
            with app.app_context():
                return self.run(self, *args, **kwargs)
    
    celery_app.conf.update(app.config)
    celery_app.autodiscover_tasks(CELERY_TASK_LIST)
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    # celery_app.Task = FlaskTask
    return celery_app