from django.db import models
from .patient import Patient

class PreviousPost(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    denomination = models.CharField(max_length=255)
    enterprise = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    nuisance_factors = models.TextField()