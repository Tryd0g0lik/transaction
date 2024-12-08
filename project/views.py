from flask import (request, jsonify)
from celery import Celery

from project.apps import app_ as app
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users

# Celery

celery = Celery(app.name, broker='redis://localhost:6379/0')

@app.router("/api/v1/create_transaction", methods=["POST"])
def create_transaction():
    data = request.json()
    user_id = data["id"]
    amount = data["amount"]
    session = get_session()

    status_text = "None"
    status = False
    try:
        # Receives the user and calculates the commission
        user = session(Users).query.filter_by(id=int(user_id)).first()
        if user:
            commission = int(amount) * user.commission_rate
            new_transaction = Transaction(
                amount=amount,
                commission=commission,
                status="ожидание"
            )
            session.add(new_transaction)
            session.commit()
            return jsonify({"message": "Transaction was created",
                            "transaction_id": new_transaction.id})
        
        
    except Exception as e:
        status_text = status_text.replace(
            "None",
            f"[create_transaction]: Something what wrong!")
    finally:
        pass
        
    