def get_celery_app():
    from project.apps import create_flask
    app = create_flask["app"]
    return app.extensions["celery"]

celery_app = get_celery_app()