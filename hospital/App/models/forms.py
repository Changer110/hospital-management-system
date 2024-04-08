
from django import forms
from App.models import *
from django.contrib.auth.forms import UserCreationForm
from App.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username','email', 'password1' ,'password2'
        ]




class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'employee_id','employee_name','enterprise_ID','birth_date','birth_place',
            'nationality','age','gender','phone_number','email','address','size','blood_group',
            'marital_status','dependent_children','affiliation_with_inss','emergency_contact',
            'hiring_date','departure_date','leaving_reason','qualification',
        ]


class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = [
            'patient','symptoms','diagnosis','treatment','doctor','price',
            'complaints','constants','physical_examination','observations'
        ]


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'  


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

  
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'  
        

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'  


class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = '__all__'  


class PreviousPostForm(forms.ModelForm):
    class Meta:
        model = PreviousPost
        fields = '__all__'
        

class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = '__all__'  


class OccupationalIllnessForm(forms.ModelForm):
    class Meta:
        model = OccupationalIllness
        fields =  '__all__'                         


class BackgroundForm(forms.ModelForm):
    class Meta:
        model = Background
        fields = '__all__'


class SummonsForm(forms.ModelForm):
    class Meta:
        model = Summons
        fields =  '__all__'


class CurrentPostForm(forms.ModelForm):
    class Meta:
        model = CurrentPost
        fields =  '__all__'


class medicalVisitForm(forms.ModelForm):
    class Meta:
        model = MedicalVisit
        fields =  '__all__'

        
class AbsenteeismForm(forms.ModelForm):
    class Meta:
        model = Absenteeism
        fields = '__all__'


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'