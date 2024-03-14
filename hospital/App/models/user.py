
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    roles = [('Doctor','Doctor')]
    role = models.CharField(max_length=10, choices=roles, default = 'Doctor', null=False)