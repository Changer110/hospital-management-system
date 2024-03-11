from django.db import models
from .medical_record import MedicalRecord
from .drugs import Drugs

class Prescription(models.Model):
    medical_record = models.ForeignKey(MedicalRecord,to_field='id' ,on_delete=models.CASCADE)
    drug_name = models.ForeignKey(Drugs, to_field='name', on_delete=models.CASCADE)
    dosage = models.PositiveIntegerField()