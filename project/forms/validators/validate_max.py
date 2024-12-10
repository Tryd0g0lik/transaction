"""This is validator checks inputs number. It is integer."""
from cfgv import ValidationError

def validate_string_max_leng(text: str, max_leng: int=255):
    """
    TODO: This is validator checks inputs number. It is integer.
    :param max_leng: int. For indicate the string max length. \n
Max length is from zero before 255. 'max_leng' has a default values is \n
which equal 255.
    :param text: str. This is length strig should be before <= 'max_leng'.
    :return: The True if 'max_length belongs to range from zero before 255 \n
or not.
    """
    status_bool = False
    try:
        if max_leng > 255:
            raise ValidationError("Max number is 255. Check your nuber")
        if max_leng == 0:
            raise ValidationError("'max_leng' is number.\
Not to be, equal to zero")
        if len(text) <= 255 and len(text) > 0:
            status_bool = True
        else:
            raise ValidationError("Check a text's length.")
    except Exception as e:
        message = f"'max_leng' is an integer. \
Mistake => {e.__str__()}"
        print(message)
        raise ValidationError(message)
    finally:
        return status_bool