
from django import forms
from App.models import *




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


class ChangePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        



class AddDrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'  



class ChangeDrugForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'  
        

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'    
        
        
  
class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'  
        
        
  
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'  
        


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
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
        
        # BackgroundPatient
        


class AccidentForm(forms.ModelForm):
    class Meta:
        model = Accident
        fields = '__all__'  



class OccupationalIllnessForm(forms.ModelForm):
    class Meta:
        model = OccupationalIllness
        fields =  '__all__'                         



class BackgroundPatientForm(forms.ModelForm):
    class Meta:
        model = BackgroundPatient
        fields = '__all__'



class SummonsFormForm(forms.ModelForm):
    class Meta:
        model = SummonsForm
        fields =  '__all__'


class CurrentPostForm(forms.ModelForm):
    class Meta:
        model = CurrentPost
        fields =  '__all__'


class medicalVisitForm(forms.ModelForm):
    class Meta:
        model = MedicalVisit
        fields =  '__all__'