"""
This page is a form for edit the user transaction data.
"""
from flask_wtf import FlaskForm
from wtforms import (
                    SelectField,
                    DateTimeField,)
from datetime import datetime
# from project.transactions import Bank
_Auto = object()
class FormEditUser_TransactionData(FlaskForm):
   
    

    user_id = SelectField(
        'User ID', coerce=int,
        choices=[]
    )
    trasaction_id = SelectField(
        "Transaction ID", coerce=int,
        choices=[]
    )
    datetime = DateTimeField("Date_time",
                             default=datetime.utcnow)

    def __init__(self, formdata=_Auto, **kwargs):
        super().__init__(formdata, **kwargs)
        # pass
        """
        Не рабочие строчки - ниже
        читать "project/transactions.py::get_user_all_"
        Предполагалось, что загруженная форма будет иметь списки ID
        """
        # bank = Bank()
        # user_list = bank.get_user_all_()
        # self.user_id.choices = [user.id if user.id else [] for user
        #                         in user_list]
        
        # self.trasaction_id.choices = [transaction.id  if transaction.id else []
        #                               for transaction
        #                               in self._get_transaction_all()
        #                               if transaction.id]
  

    def __str__(self):
        return f" Index: {self.id}, Transaction ID: {self.trasaction_id} User ID: \
    {self.user_id}"