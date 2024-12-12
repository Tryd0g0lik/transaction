"""Celery tasks by transactions"""
import logging
from project.celeries.celery import celery_init_app
# from project.apps import celery_app

# from project.celeries.make_celery import
celery_app = celery_init_app()

@celery_app.task(
    name="task_transaction_status_check",
    autoretry_for=(Exception, ),
    retry_kwargs={"max_retries": 5},
    routing_key="hard"
)
def check_pending_transaction() -> [bool]:
    from celery.worker.state import requests
    from project.transactions import Bank
    # from project.models_more.model_user_transactions import User_Transaction
    from project.models_more.model_user import Users
    from project.logs import configure_logging
    log = logging.getLogger(__name__)
    configure_logging(logging.INFO)
    # configure_logging(logging.INFO)
    bank = Bank()
    log.info("[check_pending_transaction]: opening the 'Bank' class")
    session = bank.session
    result_dict = {"message": "", "id": "", "status": "истекла"}
    log.info("[check_pending_transaction]: run the task 'check_pending_transaction' name.")
    try:
        log.info("[check_pending_transaction]: 'for transaction in bank.pending()'")
        for transaction in bank.pending():
            log.info("[check_pending_transaction]: before receiving list of all users from db  ")
            # session(Users).query.all()  # filter_by(id < 99999).first()
            user = \
                session(Users).query.all()  # filter_by(id < 99999).first()
            if not user:
                log.info("[check_pending_transaction]: User was not found")
                result_dict["massage"] = "User was not found"
                requests.post(
                    user.webhook_url, json=result_dict
                )
                return False
            log.info("[check_pending_transaction]: User was found")
            requests.post(
                user.webhook_url,
                json={"message": "", "id": str(transaction.id),
                      "status": "истекла"}
            )
    
    except Exception as e:
        print(f"Error => {e.__str__()}")
        log.info(f"Error => {e.__str__()}")
    
    finally:
        bank.close()
        log.info("[check_pending_transaction]: closed the 'Bank' class")
        
def start_first_celery_task() -> None:
    try:
        from celery.result import AsyncResult
        check_pending_transaction.apply_async(
            queue='queve_status_transaction',
            exchange='exchange_status_transaction',
        )
        resp = check_pending_transaction.delay()
        result = AsyncResult(resp.id)
    except Exception as e:
        print(f"[celery task run]: Mistake => {e.__str__()}")
    finally:
        pass