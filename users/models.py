from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  # first_name = models.CharField(max_length=20)
  # surname = models.CharField(max_length=50)
  # # join_date =  models.DateTimeField

  def __str__(self):
    return self.email