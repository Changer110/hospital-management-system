from django.shortcuts import render, redirect
from App.models import Patient

def delete_patient(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')  # Redirect to the patient list page after deletion
    return render(request, 'delete_patient.html', {'patient': patient})