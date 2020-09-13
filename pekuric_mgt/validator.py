from django.core.exceptions import ValidationError


def ExtensionValidator():
    valid_extension = ['.svg', '.pdf', '.docx', '.doc', '.jpg', '.png']
    if '.svg' or '.pdf' or '.doc'or '.jpg' or '.png' not in valid_extension:
        raise ValidationError("This file format is not supported")
    else:
        return valid_extension

