from django.db import models
from .patient import Patient

class Accident(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    date = models.DateField()
    material_causel = models.CharField(max_length=100)
    lesions_nature = models.TextField()
    position = models.CharField(max_length=100)
    days_off = models.PositiveIntegerField()
    partial_incapacity = models.CharField(max_length=5, choices = [('Yes','Yes'),('Not','Not')])
    observation = models.TextField()