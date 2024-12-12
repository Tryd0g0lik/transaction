from flask import Flask
from project.celeries.celery import celery_init_app


# def get_celery_app(app: Flask):
# def get_celery_app(app: Flask):
    
    # from project.apps import create_flask
    # app = create_flask["app"]
    # celery_app = celery_init_app(app)
    # celery_app = app_.extensions["celery"]
    # return celery_app

# celery_app = get_celery_app()
