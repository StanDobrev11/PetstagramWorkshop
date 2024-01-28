from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class MaxFileSizeValidator(BaseValidator):

    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message)
        self.limit_value = convert_mb_to_bytes(limit_value)
        self.message = f"The file size cannot be more than {limit_value} MB"

    def clean(self, file_obj):
        return file_obj.size

    def compare(self, file_size, limit_size):
        return limit_size < file_size


def convert_mb_to_bytes(value):
    return value * 1024 * 1024


def validate_photo_size(file_obj):
    max_file_size_in_mb = 5
    max_file_size_in_bites = 1024 * 1024 * max_file_size_in_mb

    if file_obj.size > max_file_size_in_bites:
        raise ValidationError(f"The file size cannot be more than {max_file_size_in_mb} MB")
