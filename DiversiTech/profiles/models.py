from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from django.contrib.postgres.fields import DateRangeField


class Tag(models.Model):
  tag_name = models.CharField(max_length=50, unique=True)

  class Meta:
      ordering = ["tag_name"]
  
  def __str__(self):
      return self.tag_name
  

class Industry(models.Model):
  industry_name = models.CharField(max_length=50, unique=True)

  class Meta:
      ordering = ["industry_name"]
  
  def __str__(self):
      return self.industry_name


class Profile(models.Model):
  class Meta:
        constraints = [
            models.UniqueConstraint(fields=['owner'], name="profiles_profile_unique")
        ]

  def __str__(self):
      return self.owner.get_username()

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
  contact_preference = models.CharField(max_length=30, choices=contact_preference_choices, default="Email")
  is_open_to_mentor = models.BooleanField(null=True, blank=True)
  is_seeking_mentorship = models.BooleanField(null=True, blank=True)
  date_created = models.DateTimeField(null=True, blank=True)

  owner = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    related_name='user_profile')
  
  industries = models.ManyToManyField(Industry, related_name='industry_profiles', blank=True)
  tags = models.ManyToManyField(Tag, related_name='tagged_profiles', blank=True)

class Experience(models.Model):
   
    experience_type_choices = (
        ("Volunteering", "Volunteering"),
        ("Project", "Project"),
        ("Talk", "Talk"),
        ("Mentoring", "Mentoring"),
        ("Job", "Job")
    )
    profile = models.ForeignKey(
      'Profile',
      on_delete=models.CASCADE,
      related_name='profile_experiences')
    
    experience_type = models.CharField(max_length=50, choices=experience_type_choices, default="Job") 
    description = models.CharField(max_length=1000, null=False, blank=False)
    url = models.URLField(null=True, blank=True)
    picture_url = models.URLField(null=True, blank=True)
    is_present_experience = models.BooleanField(null=False, blank=False, default=False)
    start_date = models.DateField(blank=False, null=False)
    end_date = models.DateField(blank=True, null=True)

    def start_date_formatted(self):
        return self.start_date.strftime("%b %Y")

    def end_date_formatted(self):
        if self.end_date:
            return self.end_date.strftime("%b %Y")
        return "Present"

    def __str__(self):
        return f"{self.description} - {self.start_date_formatted()} to {self.end_date_formatted()}"
    
    class Meta:
        verbose_name_plural = 'Experiences'
