from flask import (request, jsonify, flash, Response)
from typing import (Dict, Any)

from flask_admin.contrib.sqla import ModelView


from project.apps import app_ as app
from project.models import get_session
from project.transactions import Bank



@app.router("/api/v1/create_transaction", methods=["POST"])
def create_transaction() -> Response:
    """
    TODO: THis is logic for interface of add the new transaction.
        It's works at target through an API key
    :return: str or bool
    """
    data = request.json()
    user_id = data["id"]
    amount = data["amount"]
    
    status_text = "None"
    result_json = jsonify({"message": ""})
    if not user_id or not amount:
        status_text = status_text.replace(
            "None",
            "[create_transaction]: Not found the 'user_id' or 'amount'.\
 Need check they.")
        print(status_text)
        result_json = jsonify(
            {"message": "Not found the 'user_id' or 'amount'.\
 Need check they."})
    bank = Bank()
    try:
        resp_bool = bank.add(int(user_id), float(amount))
        if resp_bool == False:
            flash("Транзакция не добавлена", "danger")
            
            result_json = jsonify(
                {"message": "Transaction was created", })
        else:
            flash("Транзакция не добавлена", "success")
            result_json = jsonify({"message": "Transaction was created",
                            "transaction_id": bank.get_transaction()})
    except Exception as e:
        status_text = status_text.replace(
            "None",
            f"Error => {e.__str__()}")
        result_json = jsonify({"message": f"Error => {e.__str__()}"})
    finally:
        print(status_text)
        bank.close()
        return result_json
        
@app.route("/api/v1/cancel_transaction", methods=["POST"])
def cancel_transaction() -> Response:
    """
       TODO: THis is logic for interface for cansel the transaction.
           It's works at target through an API key
       :return: str or bool
       """
    data = request.json()
    transaction_id = data["transaction_id"]
    status_text = "None"
    result_json = jsonify({"message": ""})
    if not transaction_id:
        status_text = status_text.replace(
            "None",
            "[cancel_transaction]: Not found the 'transaction''.\
 Need check this."
        )
        print(status_text)
        result_json = jsonify({"message": "Transaction was created", })
        return result_json

    bank = Bank()
    try:
        resp_bool = bank.cancels(int(transaction_id))
        if resp_bool:
            status_text = "Transaction cancelled", "success"
            result_json = jsonify(
                {"message": "Transaction cancelled"}
            )
        else:
            result_json = jsonify(
                {"message": "Cannot cancel transaction"}
            )
    except Exception as e:
        status_text = status_text.replace(
            "None",
            f"Error => {e.__str__()}"
        )
        result_json = jsonify({"message": f"Error => {e.__str__()}"})
    finally:
        print(status_text)
        flash(status_text)
        bank.close()
        return result_json
    
@app.router("/api/v1/check_transaction/<int:transaktion_id>", methods=["GET"])
def check_transaction(transaction_id):
    """
    TODO: THis is logic for interface for check the transaction.
        It's works at target through an API key
    :return: str or bool
    """
    status_text = "None"
    result_json = jsonify({"message": "", "status": ""})
    if not transaction_id or (type(transaction_id) != str
                              and type(transaction_id) != int):
        status_text = status_text.replace(
            "None",
            "[check_transaction]: Not found the 'transaction''.\
 Need check this."
        )
        print(status_text)
        result_json = jsonify({"message": "Transaction was created", })
        return result_json
    bank = Bank()
    try:
        resp_dic = bank.check(int(transaction_id))
        result_json = jsonify({"message": "", "status": resp_dic["status"]})
    except Exception as e:
        status_text = status_text.replace(
            "None",
            f"Error => {e.__str__()}"
        )
        result_json = jsonify({"message": f"Error => {e.__str__()}",
                               "status": ""})
    finally:
        print(status_text)
        flash(status_text)
        bank.close()
        return result_json
