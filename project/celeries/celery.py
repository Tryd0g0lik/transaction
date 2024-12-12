from celery import Celery, Task
from flask import Flask
from dotenv_ import REDIS_URL
# The SOURCE the TASKS for LIST

CELERY_TASK_LIST = [
    "project.celeries.celery_tasks",
]

# def celery_init_app(app: Flask) -> Celery:
def celery_init_app() -> Celery:
    
    celery_app = Celery(
        "first_myCelery",
        include=CELERY_TASK_LIST,
        broker=f"{REDIS_URL}"
    )
    
    # TaskBase = celery_app.Task
    # class FlaskTask(TaskBase):
    #     def __call__(self, *args, **kwargs) -> object:
    #         with app.app_context():
    #             return self.run(self, *args, **kwargs)
    # class FlaskTask(Task):
    #     def __call__(self, *args: object, **kwargs: object) -> object:
    #         with app.app_context():
    #             return self.run(*args, **kwargs)
    # celery_app.conf.update(app.config)
    # app.config.from_mapping(
    #     CELERY=dict(
    #         broker_url=f"{REDIS_URL}",
    #         result_backend="redis://localhost",
    #         task_ignore_result=True,
    #     ),
    # )
    celery_app.conf['CELERY_TASK_SERIALIZER'] = 'json'
    celery_app.conf['CELERY_ACCEPT_CONTENT'] = ['json']
    # celery_app.config_from_object(app.config["CELERY"])
    celery_app.autodiscover_tasks(CELERY_TASK_LIST)
    celery_app.set_default()
    # app.extensions["celery"] = celery_app
    # celery_app.Task = FlaskTask
    return celery_app

