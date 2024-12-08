from flask import (request, jsonify, flash)
from celery import Celery

from project.apps import app_ as app
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users
from project.transactions import Bank

# Celery

celery = Celery(app.name, broker='redis://localhost:6379/0')

@app.router("/api/v1/create_transaction", methods=["POST"])
def create_transaction():
    data = request.json()
    user_id = data["id"]
    amount = data["amount"]
    
    status_text = "None"
    status = False
    if not user_id or not amount:
        status_text = status_text.replace(
            "None",
            "[create_transaction]: Not found the 'user_id' or 'amount'.\
 Need check they.")
        print(status_text)
        return status
    bank = Bank()
    try:
        resp_bool = bank.add_transaction(int(user_id),
                             float(amount))
        if resp_bool == False:
            flash("Транзакция не добавлена", "danger")
            return jsonify(
                {"message": "Transaction was created",}
                )
        flash("Транзакция не добавлена", "success")
        return jsonify({"message": "Transaction was created",
                        "transaction_id": bank.get_transaction()})
    
    
    except Exception as e:
        status_text = status_text.replace(
            "None",
            f"[create_transaction]: Something what wrong!")
    finally:
        print(status_text)
        bank.close()
        
    