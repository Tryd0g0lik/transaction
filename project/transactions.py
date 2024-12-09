"""
Here is a logic for work with db.
This is a management for control the transaction
"""
from typing import (Dict, Any)
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
    
    def add(self, user_id: int, amount: float) -> bool:
        status = False
        try:
            # Receives the user and calculates the commission
            user = self.session(Users).query.filter_by(id=user_id).first()
            if user:
                commission = amount * user.commission_rate
                new_transaction = Transaction(
                    amount=amount,
                    commission=commission,
                    status="ожидание"
                )
                self.session.add(new_transaction)
                self.session.commit()
                self._transaction = new_transaction.id
            print(f"[Bank]: 'add' New transaction was added, now ")
            status = True
            
        except Exception as e:
            print(f"[Bank]: 'add' Error => {e}")
        finally:
            return status
    
    def cancels(self, transaction_id: int) -> bool:
        status = None
        try:
            old_transaction = self.session(Transaction).query\
                .filter_by(transaction_id).first()
            if old_transaction and old_transaction == "ожидание":
                old_transaction.status = \
                    old_transaction.status.replace("ожидание", "отменена")
                self.session.commit()
                status = True
        except Exception as e:
            print(f"[Bank]: 'cancels' Error => {e}")
        finally:
            return status
    
    def check(self, transaction_id: int) -> Dict[str, Any]:
        status = {"status": ""}
        try:
            transaction =\
                self.session(Transaction).query.filter_by(transaction_id).first()
            if transaction:
                status["status"] =\
                    status["status"].join(str(transaction.status))
            else:
                pass
        except Exception as e:
            print(f"[Bank]: 'check' Error => {e}")
        finally:
            return status
        
    def get_transaction(self):
        """
        TODO: Receive the transaction object after add a new transaction.
        :return: object
        """
        return self._transaction
    
    def close(self):
        """Close the session"""
        try:
            self.session.close()
        except Exception as e:
            print(f"[Library]: Библиотека закрыта. Error => {e}")