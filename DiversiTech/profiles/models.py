from django.db import models

# Create your models here.
class Profile(models.Model):
  owner = models.CharField(max_length=200)
  first_name = models.CharField(max_length=30, null=False)
  last_name = models.CharField(max_length=30, null=False)
  username = models.CharField(max_length=30, null=False)
  bio = models.CharField(max_length=1800, null=False)
  location = models.JSONField()
  picture_url = models.URLField()
  is_hidden = models.BooleanField()
  number_of_endorsements = models.IntegerField()
  email_url = models.EmailField()
  facebook_url = models.URLField()
  instagram_url = models.URLField()
  github_url = models.URLField()
  linked_in_url = models.URLField()
  portfolio_url = models.URLField()
  contact_preference_selection = (
        ("Contact Form", "Contact Form"),
        ("Email", "Email"),
        ("LinkedIn", "LinkedIn"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram")
    )
  is_open_to_mentor = models.BooleanField()
  is_seeking_mentorship = models.BooleanField()
  date_created = models.DateTimeField()

 