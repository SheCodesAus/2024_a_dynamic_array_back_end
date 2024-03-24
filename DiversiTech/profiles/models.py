from django.db import models

# Create your models here.
class Profile(models.Model):
  owner = models.CharField(max_length=200)
  # first_name = models.CharField(max_length=30,null=False, blank=False)
  # last_name = models.CharField(max_length=30,null=False, blank=False)
  # username = models.CharField(max_length=30,null=False, blank=False)
  bio = models.CharField(max_length=1800, null=False, blank=False)
  location = models.CharField(max_length=50,null=True, blank=True)
  picture_url = models.URLField(null=True, blank=True)
  is_hidden = models.BooleanField(null=True, blank=True)
  number_of_endorsements = models.IntegerField(null=True, blank=True)
  email_url = models.EmailField(null=True, blank=True)
  facebook_url = models.URLField(null=True, blank=True)
  instagram_url = models.URLField(null=True, blank=True)
  github_url = models.URLField(null=True, blank=True)
  linkedin_url = models.URLField(null=True, blank=True)
  portfolio_url = models.URLField(null=True, blank=True)
  contact_preference_choices = (
        ("Contact Form", "Contact Form"),
        ("Email", "Email"),
        ("LinkedIn", "LinkedIn"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram")
    )
  contact_preference = models.CharField(max_length=30, choices=contact_preference_choices)
  is_open_to_mentor = models.BooleanField(null=True, blank=True)
  is_seeking_mentorship = models.BooleanField(null=True, blank=True)
  date_created = models.DateTimeField(null=True, blank=True)

  