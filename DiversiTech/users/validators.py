from django.core.exceptions import ValidationError
from .models import CustomUser

def validate_unique_username(value):
    """
    Custom validator to ensure case-insensitive uniqueness of usernames. 
    """

    existing_users = CustomUser.objects.filter(username__iexact=value)
    if existing_users.exists():
        raise ValidationError("This username is already taken.")