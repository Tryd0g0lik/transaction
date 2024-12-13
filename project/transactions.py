"""
Here is a logic for work with db.
This is a management for control the transaction
"""
from typing import (Dict, Any)
from project.models import get_session
from project.models_more.model_transaction import Transaction
from project.models_more.model_user import Users
from project.models_more.model_user_transactions import User_Transaction


class Bank:
    """
    TODO:" This is a management for control the transaction.
        Logics is for work to an API and only one method  \
        the 'pending' is working to the 'celery task.
    """
    def __init__(self):
        self.session = get_session()
        self._transaction = None

    def add(self, user_id: int, amount: float) -> bool:
        """
        TODO: This is the integration with db. It is when we need to make adding \
            new data to the db.
        :param user_id: int. Id of user.
        :param amount: float. It's sum of transaction.
        :return: bool If True is returning the , it means what is \
            everything OK or not if is received the False
        """
        status = False
        try:
            # Receives the user and calculates the commission
            user = self.session(Users).query.filter_by(id=user_id).first()
            if user:
                commission = amount * user.commission_rate
                # Transaction
                new_transaction = Transaction(
                    amount=amount,
                    commission=commission,
                    status="ожидание"
                )
                self.session.add(new_transaction)
                self.session.commit()
                user_transaction = User_Transaction(
                    user_id=user.id,
                    trasaction_id=new_transaction,
                )
                # User_Transaction average
                self.session.add(user_transaction)
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
    
    def pending(self):
        """
        Ошибка. Вызывая метод в celery задачи session НЕ рабочая!
        
        :return:
        """
        from datetime import datetime, timedelta
        
        try:
            panding_transaction = \
                self.session(User_Transaction).query.filter_by(
                    status='ожидание'
                    ).all()
            if len(panding_transaction) == 0:
                return panding_transaction
            """
           panding_transaction
           Получаем список id-транзакций, id-пользлвателей,  время\
            регистрации транзакции (при налиции \
           данных в базе данных)
           
           """
            for user_transaction in panding_transaction:
                if datetime.now() - user_transaction.created_at >\
                    timedelta(minutes=15):
                    transaction = self.session(Transaction).query\
                        .filter_by(id=user_transaction.trasaction_id)
                    yield transaction
                    transaction.status = "истекла"
                    self.session.commit()
        except Exception as e:
            print(f"[Bank]: 'check' Error => {e}")
        finally:
            pass
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

    
