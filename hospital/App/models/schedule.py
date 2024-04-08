
from django.db import models
from .doctor import Doctor


class Schedule(models.Model):
    days = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]
    doctor = models.ForeignKey(Doctor, to_field = 'doctor_id', on_delete=models.CASCADE)
    day = models.CharField(max_length = 20, choices = days)
    from_time = models.TimeField()
    to_time = models.TimeField()
    patient_limit = models.PositiveIntegerField()
    