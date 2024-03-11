from django.db import models
from .patient import Patient

class SummonsForm(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    motif = models.CharField(max_length=255)
    date_of_issue = models.DateField()
    date_of_summons = models.DateField()
    date_de_presentation = models.DateField()
    observation = models.TextField()