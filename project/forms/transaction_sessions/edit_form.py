"""
This page is a form for edit the transaction data.
"""
from flask_wtf import FlaskForm
from wtforms import (
                    SelectField,
                     FloatField,
                     validators)
from project.models import get_session
# from project.views import get_user_all

# session = get_session()
form_choices = {
    'Transaction': [
        ("NON", "----"),
        ("EXP", "истекла"),
        ("CAN", "отменена"),
        ("DENO", "подтверждена"),
        ("WAIT", "ожидание")
    ]
}
#
# users = {
#     "users":get_user_all()
# }
# This is a TEST FORM !
class FormEditorTransactionData(FlaskForm):
    
    def __init__(self, *args,):
        super(FormEditorTransactionData, self).__init__(args)
        self.user_id.choices = self.get_user_all()
        
    amount = FloatField("Sum",
                        default="0.0",
                        validators=[
                            validators.InputRequired()
                        ],
                        description="It is a sum of the transaction."
                        )
    commission = FloatField("Commission",
                            default="0.05",
                            validators=[
                                validators.InputRequired()
                            ],
                            description="It is s size of commission for \
transaction"
                            )
    status = SelectField("Status",
                         default="----",
                         validators=[
                             validators.InputRequired(),
                         ],
                         choices=form_choices,
                         )
    
    user_id = SelectField('User', coerce=int,
                          choices=[])
    
    
    #
    def get_user_all(self) -> list :
        from project.apps import get_session
        from project.models_more.model_user import Users
        session = get_session()
        user_list = session(Users).query.all()
        return user_list