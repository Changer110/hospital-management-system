from django.db import models
from .doctor import Doctor
from .patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient , on_delete=models.CASCADE, to_field='employee_id')
    doctor = models.ForeignKey(Doctor, to_field = 'doctor_id', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    