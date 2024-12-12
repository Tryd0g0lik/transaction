"""Celery tasks by transactions"""

from project.models_more.model_user_transactions import User_Transaction
from project.transactions import Bank


def check_pending_transaction() -> [bool]:
    from celery.worker.state import requests
    from project.models_more.model_user import Users
    bank = Bank()
    session = bank.session
    result_dict = {"message": "", "id": "", "status": "истекла"}
    
    try:
        
        for transaction in bank.pending():
            # session(Users).query.all()  # filter_by(id < 99999).first()
            user = \
                session(User_Transaction).query.all()  # filter_by(id < 99999).first()
        if not user:
            result_dict["massage"] = "User was not found"
            requests.post(
                user.webhook_url, json=result_dict
            )
            return False
        requests.post(
            user.webhook_url,
            json={"message": "", "id": str(transaction.id),
                  "status": "истекла"}
        )
    
    except Exception as e:
        print(f"Error => {e.__str__()}")
    
    finally:
        bank.close()