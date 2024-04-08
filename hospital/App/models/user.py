
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    roles = [
        ('Admin','Admin'),
        ('Doctor','Doctor'),
        ('Nurse','Nurse')]
    role = models.CharField(max_length=10, choices=roles, default = 'Admin', null=False)

    
    
    
