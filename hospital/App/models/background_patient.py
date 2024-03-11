from django.db import models
from .patient import Patient

class BackgroundPatient(models.Model):
    employee_id = models.ForeignKey(Patient, to_field = 'employee_id', on_delete=models.CASCADE)
    personal_medical = models.TextField()
    personal_surgical = models.TextField()
    proffesional_medical = models.TextField()
    proffesional_surgical = models.TextField()
    family_medical = models.TextField()
    family_surgical = models.TextField()
    social_personal = models.TextField()
    social_family = models.TextField()
