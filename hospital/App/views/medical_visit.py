

from django.shortcuts import render, redirect
from App.models import *


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
        form = MedicalVisit(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_visit',employee_id=employee_id)
    return render(request, 'add_medical_visit.html', context)