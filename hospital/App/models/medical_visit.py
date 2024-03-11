
from django.db import models
from .patient import Patient
from .doctor import Doctor

class MedicalVisit(models.Model):
    employee_id = models.ForeignKey(Patient, on_delete=models.CASCADE, to_field='employee_id')
    plaintes = models.TextField()
    mensuration_kg = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_size = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_TA = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_PIT = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_PTE = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_PA = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_Pouls = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_AV_OD = models.DecimalField(max_digits = 3, decimal_places=2)
    mensuration_OG = models.DecimalField(max_digits = 3, decimal_places=2)
    
    biology = models.TextField()
    electrocardiogram = models.TextField()
    audiometry = models.TextField()
    spirometry = models.TextField()
    RX_pulmonery = models.TextField()
    
    what_to_do = models.TextField()
    aptitude = models.TextField()
    doctor = models.ForeignKey(Doctor,to_field='doctor_id',on_delete=models.CASCADE)