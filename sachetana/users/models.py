from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    registration_number = models.CharField(max_length=100, unique=True)
  

    USERNAME_FIELD = 'registration_number'
    REQUIRED_FIELDS = ['password'] 

    def __str__(self):
        return self.registration_number
