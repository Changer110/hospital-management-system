

from django.shortcuts import render, redirect
from App.models import *
from App.models.forms import medicalVisitForm



def show_medical_visit(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    medical_visits = MedicalVisit.objects.filter(employee_id = employee_id)
    context = {'visits': medical_visits, 'patient': patient}
    return render(request, 'medical_visit.html', context)


def add_medical_visit(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    doctors = Doctor.objects.all()
    context = {'patient': patient, 'doctors': doctors}
    if request.method == 'POST':
        form = medicalVisitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_visit',employee_id=employee_id)
    return render(request, 'add_medical_visit.html', context)


def change_medical_visit(request,visit_id):
    try:
       medical_visit = MedicalVisit.objects.get(id=visit_id)
    except MedicalVisit.DoesNotExist:
        return redirect('medical_visit')  # Redirect to medical_record page if record doesn't exist

    if request.method == 'POST':
        form =medicalVisitForm(request.POST, instance=medical_visit)
        if form.is_valid():
            form.save()
            return redirect('medical_visit', employee_id =medical_visit.employee_id.employee_id)
    else:
        form = medicalVisitForm(instance=medical_visit)

    return render(request, 'change_medical_visit.html', {'form': form, 'medical_visit': medical_visit})


def delete_medical_visit(request, visit_id):
    try:
        medical_visit = MedicalVisit.objects.get(id=visit_id)
    except MedicalVisit.DoesNotExist:
        return redirect('medical_visit')  # Redirect to medical_visit list view if record doesn't exist

    if request.method == 'POST':
        medical_visit.delete()
        return redirect('medical_visit', employee_id=medical_visit.employee_id.employee_id)  # Replace 'medical_visit' with the appropriate URL pattern name for the medical visit list view

    context = {'medical_visit': medical_visit}
    return render(request, 'delete_medical_visit.html', context)
