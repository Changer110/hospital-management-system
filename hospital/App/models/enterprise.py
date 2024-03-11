from django.db import models

class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    enterprise_ID = models.CharField(max_length=100, unique = True)