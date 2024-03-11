# from django.db import models

# class Patient(models.Model) :
#     name = models.CharField(max_length=100)
#     age  = models.IntegerField()
#     gender = models.CharField(max_length=10)
#     phone_number=models.CharField(max_length=20)
#     email =models.EmailField()
#     address=models.CharField(max_length=200)
#     date_admitted =models.DateField()
#     is_active=models.BooleanField(default=True)



# class Doctor(models.Model):
#     name=models.CharField(max_length=100)
#     specialization= models.CharField(max_length=100)
#     phone_number=models.CharField(max_length=20)
    
    
    
# class Appointment(models.Model):
#     patient =models.ForeignKey(Patient, to_field='id', on_delete=models.CASCADE)
#     doctor= models.ForeignKey(Doctor,to_field='id', on_delete=models.CASCADE)
#     Appointment_date=models.DateTimeField()
    


# class Department(models.Model):
#     patient= models.ForeignKey(Patient, to_field='id' ,on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
    


# class MedicalRecord(models.Model):
#     patient = models.ForeignKey(Patient, to_field='id' ,on_delete=models.CASCADE)
#     symptoms= models.TextField()
#     diagnosis = models.TextField()
    
    
  

# class Drugs(models.Model):
#     name =models.CharField(max_length=100,unique=True)
#     quantity =models.PositiveIntegerField()
#     expiry_date =models.DateField()
#     dosage_issued=models.PositiveIntegerField(default=0)
    
    
    
    
# class Prescription(models.Model):
#     medical_record =models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
#     medication = models.ForeignKey(Drugs,to_field='name', on_delete=models.CASCADE)
#     dosage= models.PositiveIntegerField()
    
    
    