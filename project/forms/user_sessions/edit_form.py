"""
This page is a form for edit the user data.
"""
from flask_wtf import FlaskForm
from wtforms import (StringField,
                     SubmitField,
                     FloatField,
                     validators)

from project.forms.validators.validate_max import validate_string_max_leng
from project.forms.validators.validate_min import validate_string_min_leng



class FormEditorUserData(FlaskForm):
    balance = FloatField("balance",
                         validators=[
                             validators.InputRequired()
                         ],
                         description="By default values is  0.0"
                         )
    commission_rate = FloatField("commission",
                                 validators=[
                                     validators.InputRequired(),
                                 ],
                                 description="By default values is  0.05")
    webhook_url = StringField(
        "webhook_url",
        validators=[
            validators.InputRequired(),
        ],
        description="By default values is 'http://example.com/webhook'. \
Min 3 symbol and max 255"
    )
    wallet_address = StringField(
        "wallet_address",
        validators=[
            validators.InputRequired(),
        ],
        description="By default values is '	test_wallet' \
Min 3 symbol and max 255"
    )
    # submit = SubmitField("Save",
    #                      render_kw={"class": "btn btn-secondary"})
    def validator_text_length(self, webhook_url: str,
                              max_len: int = 255, min_len:int = 3):
        """
        TODO: This is validator checks inputs number. It is integer.
        :param max_leng: int. For indicate the string max length. \n
Max length is from zero before 255. 'max_leng' has a default values is \n
which equal 255.
        :param min_leng: int. For indicate the string min length. \n
Min length is from 3. 'min_leng' has a default values is \n
which equal 3.
        :param webhook_url: str. This is length strig should be \n
from 'min_len' and before <= 'max_leng'.
        :return: The True if 'max_length belongs to range from 'min_len' \n
before 'max_len' or not.
        """
        result_max_bool = validate_string_max_leng(webhook_url, max_len)
        result_min_bool = validate_string_min_leng(webhook_url, min_len)
        
        if not result_max_bool or not result_min_bool:
            raise ValueError("Mistake of 'validator_text_length' to values!")
    