from rest_framework.exceptions import ValidationError

def raise_exception(message):
    raise ValidationError({"message": message})