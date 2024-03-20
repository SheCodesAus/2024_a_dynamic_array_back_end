from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    accepted_terms = models.BooleanField(default=False)

def __str__(self):
    return self.username

