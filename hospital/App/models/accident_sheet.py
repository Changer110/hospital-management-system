from django.db import models
from .patient import Patient

class Accident(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    date = models.DateField()
    causal_material_element = models.CharField(max_length=100)
    nature_of_lesions = models.TextField()
    position = models.CharField(max_length=100)
    numb_of_days_off = models.PositiveIntegerField()
    partial_permanent_incapacity = models.BooleanField()
    observation = models.TextField()