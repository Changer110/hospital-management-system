from django.shortcuts import render,redirect
from App.models import BackgroundPatient, Patient


def background_patient(request, employee_id):

  patient = Patient.objects.get(employee_id=employee_id)
  background_patients = BackgroundPatient.objects.filter(employee_id=employee_id)
  context = {'background_patients': background_patients, 'patient': patient}
  return render(request, 'background_patient.html', context)



from App.models.forms import BackgroundPatientForm

def add_background_patient(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    context = {'patient': patient}
    if request.method == 'POST':
        form = BackgroundPatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('background_patient', employee_id=employee_id)
    return render(request, 'add_background_patient.html', context)