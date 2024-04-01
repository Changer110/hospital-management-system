from django.db import models
from .patient import Patient

class Summons(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    motif = models.CharField(max_length=255)
    issue_date = models.DateField()
    summons_date = models.DateField()
    presentation_date = models.DateField()
    observation = models.TextField()