"""This is validator checks inputs number. It is integer."""
from cfgv import ValidationError

def validate_string_min_leng(text: str, min_leng: int=3):
    """
    TODO: This is validator checks inputs number. It is integer.
    :param min_leng: int. For indicate the string min length. \n
Min length is from 3. 'min_leng' has a default values is \n
which equal 3.
    :param text: str. This is length strig should be before >= 'min_leng'.
    :return: The True if 'min_length belongs to range from 3 \n
or not.
    """
    status_bool = False
    try:
        if min_leng > 3:
            raise ValidationError("Min number is 3. Check your nuber")
        if len(text) >= 3:
            status_bool = True
        else:
            raise ValidationError("Check a text's length.")        
    except Exception as e:
        message = f"'min_leng' is an integer. \
Mistake => {e.__str__()}"
        print(message)
        raise ValidationError(message)
    finally:
        return status_bool