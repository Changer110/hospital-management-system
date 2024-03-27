

from django.shortcuts import render, redirect, get_object_or_404
from App.models import *
from App.models.forms import PatientForm
from django.http import HttpResponseRedirect
from django.conf import settings
from datetime import datetime
from dateutil import parser
import os





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
            try:
                pic = request.FILES['picture']
                img_file = os.path.join(settings.BASE_DIR, 'App/static/img', pic.name)
                with open(img_file, 'wb+') as file:
                    for chunk in pic.chunks():
                        file.write(chunk)
                patient = Patient(
                    employee_id = request.POST['employee_id'], picture = pic.name,
                    enterprise_name_id = request.POST['enterprise_name'], 
                    name = request.POST['name'], age = request.POST['age'],
                    date_of_birth = request.POST['date_of_birth'],
                    place_of_birth = request.POST['place_of_birth'],
                    nationality = request.POST['nationality'], 
                    gender = request.POST['gender'],
                    phone_number = request.POST['phone_number'],
                    email = request.POST['email'], 
                    address = request.POST['address'],
                    size = request.POST['size'],
                    blood_group = request.POST['blood_group'],
                    marital_status = request.POST['marital_status'],
                    num_dependent_children = request.POST['num_dependent_children'],
                    affiliation_with_inss = request.POST['affiliation_with_inss'],
                    emergency_contact = request.POST['emergency_contact'],
                    hiring_date = request.POST['hiring_date'], 
                    departure_date = request.POST['departure_date'], 
                    reason_for_leaving = request.POST['reason_for_leaving'],
                    qualification = request.POST['qualification'], 
                    patient_creation_date = request.POST['patient_creation_date']
                )
                patient.save()
                return redirect('patient', employee_id = patient.employee_id)
            except:
                return redirect('add_patient')
        return render(request, 'add_patient.html', {'enterprises': Enterprise.objects.all()})
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
            
            # pic = request.FILES['picture']
            # img_file = os.path.join(settings.BASE_DIR, 'App/static/img', pic.name)
            # with open(img_file, 'wb+') as file:
            #     for chunk in pic.chunks():
            #         file.write(chunk)
                    

            # patient.picture = pic.name,
            # try:
                patient.name = request.POST['name'] 
                patient.age = request.POST['age']
                patient.date_of_birth = convert_date(request.POST['date_of_birth'])
                patient.place_of_birth = request.POST['place_of_birth']
                patient.nationality = request.POST['nationality']
                patient.gender = request.POST['gender']
                patient.phone_number = request.POST['phone_number']
                patient.email = request.POST['email']
                patient.address = request.POST['address']
                patient.size = request.POST['size']
                patient.blood_group = request.POST['blood_group']
                patient.marital_status = request.POST['marital_status']
                patient.num_dependent_children = request.POST['num_dependent_children']
                patient.affiliation_with_inss = request.POST['affiliation_with_inss']
                patient.emergency_contact = request.POST['emergency_contact']
                patient.hiring_date = convert_date(request.POST['hiring_date'])
                patient.departure_date = convert_date(request.POST['departure_date'])
                patient.reason_for_leaving = request.POST['reason_for_leaving']
                patient.qualification = request.POST['qualification']
                patient.save()
                return redirect('patient')
            # except:
                return redirect('change_patient', employee_id = patient.employee_id)
        return render(request, 'change_patient.html', {'patient': patient})
    return redirect('login')




def search_patient(request):
    if request.session.get('user'):
        employee_id = 'all'
        if request.method == 'POST':
            ID = request.POST.get('employee_id')
            employee_id = ID if ID else employee_id
        return redirect('patient', employee_id = employee_id)
    return redirect('login')




def convert_date(value):
    date = parser.parse(Value).strftime("%Y-%m-%d")
    return datetime.strptime(value, "%Y-%m-%d").date()