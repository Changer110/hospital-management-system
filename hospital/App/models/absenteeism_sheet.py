from django.db import models
from .patient import Patient

class Absenteeism(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    type = models.CharField(max_length=100)
    cause = models.TextField()
    beginning = models.DateField()
    reprise = models.DateField()
    days_off = models.PositiveIntegerField()