from django.db import models

class Doctor(models.Model):
    doctor_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, default='unknown')
    address = models.CharField(max_length=200, default='unknown')
    
    def __str__(self):
        return f"{self.doctor_id} - {self.name}"