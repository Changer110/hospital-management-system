


from App.models import MedicalRecord
from django.shortcuts import render, redirect
from App.models import Patient, Doctor
from App.models.forms import MedicalRecordForm
from django.db.models import Sum

from datetime import datetime
from App.models import Prescription








def display_medical_record(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        records = MedicalRecord.objects.filter(patient = employee_id)
        total_price = records.aggregate(total_price=Sum('price'))
        total_price = 0 if not total_price['total_price'] else total_price['total_price']
        context = {'records': records,'patient': patient, 'total_price' : total_price}
        return render(request, 'medical_record.html', context)
    return redirect('login')


def add_medical_record(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        doctors = Doctor.objects.all()
        context = {'patient': patient, 'doctors': doctors}
        if request.method == 'POST':
            form = MedicalRecordForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('medical_record',employee_id=employee_id)
        return render(request, 'add_medical_record.html', context)
    return redirect('login')


def delete_medical_record(request, record_id):
    if request.session.get('user'):
        try:
            records = MedicalRecord.objects.get(id=record_id)
            patient_id = records.patient.employee_id
        except MedicalRecord.DoesNotExist:
            return redirect('medical_record')  # Redirect to medical_record page if record doesn't exist

        if request.method == 'POST':
            records.delete()
            return redirect('medical_record', employee_id=patient_id)

        return render(request, 'delete_medical_record.html', {'record': records})
    return redirect('login')



def change_medical_record(request, record_id):
    if request.session.get('user'):
        try:
            records = MedicalRecord.objects.get(id=record_id)
        except MedicalRecord.DoesNotExist:
            return redirect('medical_record')  # Redirect to medical_record page if record doesn't exist

        if request.method == 'POST':
            form = MedicalRecordForm(request.POST, instance=records)
            if form.is_valid():
                form.save()
                return redirect('medical_record', employee_id = records.patient.employee_id)
        else:
            form = MedicalRecordForm(instance=records)

        return render(request, 'change_medical_record.html', {'form': form, 'record': records})
    return redirect('login')



def search_medical_record(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        if request.method == 'POST':
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            if end_date >= start_date:
                records = MedicalRecord.objects.filter(
                    patient = employee_id,
                    date__range=(start_date, end_date))
                total_price = records.aggregate(total_price=Sum('price'))
                total_price = 0 if not total_price['total_price'] else total_price['total_price']
                context = {'records': records,'patient': patient, 'total_price' : total_price}
                return render(request, 'medical_record.html', context)
                # return redirect('medical_record', employee_id=employee_id)
        return redirect('medical_record', employee_id=employee_id)
    return redirect('login')



def back_to_medical_record(request,record_id):
    if request.session.get('user'):
        records = MedicalRecord.objects.filter(id=record_id)
        patient = records.first().patient
        total_price = records.first().price
        context = {'records': records,'patient': patient, 'total_price' : total_price}
        return render(request, 'medical_record.html',context)
    return redirect('login')


def show_all_medical_records(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        records = MedicalRecord.objects.filter(patient=employee_id)
        total_price = records.aggregate(total_price=Sum('price'))
        total_price = 0 if not total_price['total_price'] else total_price['total_price']
        context = {'records': records, 'patient': patient, 'total_price': total_price}
        return render(request, 'medical_record.html', context)
    return redirect('login')