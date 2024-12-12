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
class FormEditTransactionData(FlaskForm):
    
   
        
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

    