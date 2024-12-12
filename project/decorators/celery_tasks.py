from typing import Callable, Any
from celery import Celery
def transaction_pending_wraper(app):
    def wrapper(fun: Callable[[], Any]):
        celery = Celery(app.name, broker='redis://localhost:6379/0')
        
        @celery.task
        def task_list_transaction_live():
            return fun()
        
        return task_list_transaction_live.delay()
    
    return wrapper

# Celery