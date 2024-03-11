from django.db import models
from .medical_record import MedicalRecord


class Vaccination(models.Model):
    medical_record = models.ForeignKey(MedicalRecord,to_field='id' ,on_delete=models.CASCADE)
    date = models.DateField()
    vaccine = models.CharField(max_length=100)
    lot = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    dose = models.IntegerField()