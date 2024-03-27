
from django.db import models
from .enterprise import Enterprise

class Patient(models.Model):
    employee_id = models.BigIntegerField(unique=True)
    picture = models.ImageField(upload_to='img/',null=False, blank=True)
    enterprise_name = models.ForeignKey(Enterprise, to_field = 'enterprise_ID',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = [('Male', 'Male'),('Female','Female')])
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)
    num_dependent_children = models.IntegerField()
    affiliation_with_inss = models.CharField(max_length=100)
    emergency_contact = models.CharField(max_length=200)
    hiring_date = models.DateField()
    departure_date = models.DateField()
    reason_for_leaving = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    patient_creation_date = models.DateField()

    
    def __str__(self):
        return f"{self.employee_id} - {self.name}"