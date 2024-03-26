from django.core.exceptions import ValidationError
from .models import Tag

def validate_industries(self):
    """
    Validate the industries field to ensure no more than three industries are selected.
    """
    industry_count = self.industries.count()

    if industry_count > 3:
        raise ValidationError("You may only select a maximum of three industries.")

def validate_unique_tag(value):
    cleaned_value = value.replace(" ", "").lower()
    existing_tags = Tag.objects.filter(title__icontains=cleaned_value)
    
    if existing_tags.exists():
        raise ValidationError("A similar tag title already exists")