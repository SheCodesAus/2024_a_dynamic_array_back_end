from django.core.exceptions import ValidationError
from .models import Tag, Industry

def validate_industries(self):
    """
    Validate the industries field to ensure no more than three industries are selected.
    """
    industry_count = self.industries.count()

    if industry_count > 3:
        raise ValidationError("You may only select a maximum of three industries.")

def validate_unique_tag(value):
    cleaned_value = value.replace(" ", "").lower()
    existing_tags = Tag.objects.filter(tag_name__icontains=cleaned_value)
    
    if existing_tags.exists():
        raise ValidationError("A similar tag name already exists")
    
def validate_unique_industry(value):
    cleaned_value = value.replace(" ", "").lower()
    existing_industries = Industry.objects.filter(industry_name__icontains=cleaned_value)
    
    if existing_industries.exists():
        raise ValidationError("A similar industry name already exists")