from django.core.exceptions import ValidationError

def validate_industries(self):
    """
    Validate the industries field to ensure no more than three industries are selected.
    """
    industry_count = self.industries.count()

    if industry_count > 3:
        raise ValidationError("You may only select a maximum of three industries.")
    