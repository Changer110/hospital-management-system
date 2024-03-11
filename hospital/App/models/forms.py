from django import forms
from App.models import Patient



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        
        


class DeletePatientForm(forms.Form):
    employee_id = forms.IntegerField()

    def delete_patient(self):
        employee_id = self.cleaned_data['employee_id']
        patient = Patient.objects.get(employee_id=employee_id)
        patient.delete()       
        
        
        

from App.models import Patient

class ChangePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'      
        

from App.models import Drugs

class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'  
        
        
        

class ChangeDrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'  
        

from App.models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'    
        
        
  

from App.models.medical_record import MedicalRecord

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'  
        
        
  
       
        
        
        
    
from App.models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'  
        
        
        
 
from App.models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'  
        
        
        
from App.models import Vaccination

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'  
        
        
        
from App.models import Enterprise

class EnterpriseForm(forms.ModelForm):
    class Meta:
        model = Enterprise
        fields = '__all__'  
        
        
        
        
from App.models import PreviousPost

class PreviousPostForm(forms.ModelForm):
    class Meta:
        model = PreviousPost
        fields = '__all__'     
        
        
        
from App.models import Accident

class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = '__all__'  
        
        
from App.models import OccupationalIllness

class OccupationalIllnessForm(forms.ModelForm):
    class Meta:
        model = OccupationalIllness
        fields =  '__all__'                         
        
        
        
from App.models import BackgroundPatient

class BackgroundPatientForm(forms.ModelForm):
    class Meta:
        model = BackgroundPatient
        fields = '__all__'
        
    personal_medical = forms.CharField(
        label='Personal Medical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    personal_surgical = forms.CharField(
        label='Personal Surgical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    professional_medical = forms.CharField(
        label='Professional Medical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    professional_surgical = forms.CharField(
        label='Professional Surgical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    family_medical = forms.CharField(
        label='Family Medical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    family_surgical = forms.CharField(
        label='Family Surgical',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    social_personal = forms.CharField(
        label='Social Personal',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    )
    
    social_family = forms.CharField(
        label='Social Family',
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
    ) 
    
    
    
    
    
from App.models import SummonsForm

class SummonsFormForm(forms.ModelForm):
    class Meta:
        model = SummonsForm
        fields =  '__all__'         