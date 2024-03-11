from django.db import models
from .patient import Patient
from .doctor import Doctor

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    symptoms = models.TextField()
    diagnosis = models.TextField()
    date = models.DateField()
    treatment = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,to_field='doctor_id')
    price = models.DecimalField(max_digits=15, decimal_places=2)
    complaints = models.TextField()
    constants = models.TextField()
    physical_examination = models.TextField()
    observations = models.TextField()