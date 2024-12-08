"""
Here is a logic for work with db.
This is a management for control the transaction
"""
from flask import jsonify
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users

class Bank:
    """
    This is a management for control the transaction
    """
    def __init__(self):
        self.session = get_session()
        self._transaction = None
    
    def add_transaction(self, user_id, amount) -> bool:
        status = False
        try:
            # Receives the user and calculates the commission
            user = self.session(Users).query.filter_by(id=int(user_id)).first()
            if user:
                commission = int(amount) * user.commission_rate
                new_transaction = Transaction(
                    amount=amount,
                    commission=commission,
                    status="ожидание"
                )
                self.session.add(new_transaction)
                self.session.commit()
                # return jsonify(
                #     {"message": "Transaction was created",
                #      "transaction_id": new_transaction.id}
                #     )
                self._transaction = new_transaction.id
            print(f"[Bank]: 'add_transaction' New transaction was added, now ")
            status = True
        except Exception as e:
            print(f"[Bank]: 'add_transaction' Error => {e}")
        finally:
            return status
    
    def get_transaction(self):
        return self._transaction

    def close(self):
        """Close the session"""
        try:
            self.session.close()
        except Exception as e:
            print(f"[Library]: Библиотека закрыта. Error => {e}")