from typing import Callable, Any
from celery import Celery
from dotenv_ import REDIS_URL
def transaction_pending_wraper(app):
    def wrapper(fun):
        celery = Celery(app.name, broker=f"{REDIS_URL}")
        
        @celery.task
        async def task_list_transaction_live():
            return fun()
        
        return task_list_transaction_live.apply_async(
            queve="status_transaction",
            countdown=1,
            time_limit=5
        )
    
    return wrapper

# Celery