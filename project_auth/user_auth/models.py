from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

    
USER_TYPE_CHOICES = [
      ( 'ADMIN', 'ADMIN'),
      ( 'END_USER', 'END_USER'),
]

class CustomUser(AbstractUser):
  
    roles = models.CharField(max_length=255,choices=USER_TYPE_CHOICES,null=True, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.username
    

class FileDrive(models.Model):
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.location   
