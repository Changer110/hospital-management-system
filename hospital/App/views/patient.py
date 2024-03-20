

from django.shortcuts import render, redirect, get_object_or_404
from App.models import *
from App.models.forms import PatientForm
from django.http import HttpResponseRedirect





def display_patient(request, employee_id):
    if request.session.get('user'):
        try:
            patients = Patient.objects.filter(employee_id = int(employee_id))
        except:
            patients = Patient.objects.all()
        context = {'patients': patients}
        return render(request, 'patient.html', context)
    return redirect('login')




def add_patient(request):
    if request.session.get('user'):
        if request.method == 'POST':
            form = PatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('patient')
        else:
            form = PatientForm()
        
        context = {'enterprises': Enterprise.objects.all()}
        return render(request, 'add_patient.html', context)
    return redirect('login')




def delete_patient(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        if request.method == 'POST':
            patient.delete()
            return redirect('patient')
        return render(request, 'delete_patient.html', {'patient': patient})
    return redirect('login')




def update_patient(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/patient')  # Redirect to the patient page after successful modification
        else:
            form = PatientForm(instance=patient)
        return render(request, 'change_patient.html', {'form': form})
    return redirect('login')





def search_patient(request):
    if request.session.get('user'):
        employee_id = 'all'
        if request.method == 'POST':
            ID = request.POST.get('employee_id')
            employee_id = ID if ID else employee_id
        return redirect('patient', employee_id = employee_id)
    return redirect('login')









def show_all_patient(request):
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients})

def patient_information(request, employee_id):
    patients = Patient.objects.filter(employee_id=employee_id)
    context = {'patients': patients}
    return render(request, 'patient.html', context)
    