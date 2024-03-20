from django.shortcuts import render,redirect
from App.models import BackgroundPatient, Patient


def display_background_patient(request, employee_id):
    if request.session.get('user'):

        patient = Patient.objects.get(employee_id=employee_id)
        background_patients = BackgroundPatient.objects.filter(employee_id=employee_id)
        context = {'background_patients': background_patients, 'patient': patient}
        return render(request, 'background_patient.html', context)
    return redirect('login')



from App.models.forms import BackgroundPatientForm

def add_background_patient(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        context = {'patient': patient}
        if request.method == 'POST':
            form = BackgroundPatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('background_patient', employee_id=employee_id)
        return render(request, 'add_background_patient.html', context)
    return redirect('login')
  
  
  
  
def change_background_patient(request, background_patient_id):
    if request.session.get('user'):
        background_patient = BackgroundPatient.objects.get(id=background_patient_id)

        if request.method == 'POST':
            form = BackgroundPatientForm(request.POST, instance=background_patient)
            if form.is_valid():
                form.save()
                return redirect('background_patient', employee_id=background_patient.employee_id.employee_id)
        else:
            form = BackgroundPatientForm(instance=background_patient)

        context = {'form': form, ' background_patient':  background_patient}
        return render(request, 'change_background_patient.html', context)
    return redirect('login') 
  
  
def delete_background_patient(request, background_patient_id):
    if request.session.get('user'):
        background_patient  = BackgroundPatient.objects.get(id=background_patient_id)

        if request.method == 'POST':
            background_patient.delete()
            return redirect('background_patient',employee_id=background_patient.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'background_patient': background_patient}
        return render(request, 'delete_background.html', context)
    return redirect('login')       