"""
This page is a form for edit the transaction data.
"""
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                    SelectField,
                     FloatField,
                     validators)
#
form_choices = {
    'Transaction': [
        ("NON", "----"),
        ("EXP", "истекла"),
        ("CAN", "отменена"),
        ("DENO", "подтверждена"),
        ("WAIT", "ожидание")
    ]
}
# This is a TEST FORM !
class FormEditorTransactionData(FlaskForm):
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
    