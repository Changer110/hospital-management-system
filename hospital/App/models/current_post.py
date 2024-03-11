
from django.db import models
from .patient import Patient

class CurrentPost(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    begin_date = models.DateField()
    end_date = models.DateField()
    post = models.CharField(max_length = 100)
    tasks = models.TextField()
    work_rate = models.TextField()
    nusance_factors = models.TextField()
    metrology_date = models.DateField()
    metrology_type = models.CharField(max_length = 100)
    metrology_R = models.TextField()