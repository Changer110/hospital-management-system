from django.db import models
from .patient import Patient

class OccupationalIllness(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    date = models.DateField()
    maladie = models.CharField(max_length=100)
    tableau = models.CharField(max_length=100)
    causal_agent = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    decision = models.TextField()