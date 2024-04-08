

from .import_all import *


def display_medical_record(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        records = MedicalRecord.objects.filter(patient = employee_id)
        # try:
        #     records = MedicalRecord.objects.filter(employee_id = employee_id, pk = int(record))
        # except:
        if request.session.get('dates'):
            try:
                begin = convert_date(request.session['dates']['begin'])
                end = convert_date(request.session['dates']['end'])
                if end >= begin:
                    records = MedicalRecord.objects.filter(
                        patient = employee_id,
                        date__range = (begin, end)
                    )
                request.session['dates'] = None
            except:
                records = records
        total_price = records.aggregate(total_price=Sum('price'))
        total_price = 0 if not total_price['total_price'] else total_price['total_price']
        
        context = {'records': records,'patient': patient, 'total_price' : total_price, 'list':(list(records))}
        return render(request, 'medical_record.html', context)
    return redirect('login')



def add_medical_record(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = MedicalRecordForm(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.date = date_time_now()
                record.save()
                return redirect('display_medical_record', employee_id = employee_id)
            return redirect('add_medical_record', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'record' : employee_id,
            'sbt' : 'add_medical_record',
            'doctors': Doctor.objects.all(),
            'patient': Patient.objects.get(employee_id=employee_id),
        }
        return render(request, 'medical_record_form.html', context)
    return redirect('login')





def change_medical_record(request, record_id):
    if request.session.get('user'):
        try:
            record = MedicalRecord.objects.get(pk = record_id)
        except MedicalRecord.DoesNotExist:
            return redirect('medical_record')

        if request.method == 'POST':
            form = MedicalRecordForm(request.POST, instance = record)
            if form.is_valid():
                form.save()
                return redirect('display_medical_record', employee_id = record.patient.employee_id)
            return redirect('update_medical_record', record_id = record_id)
        context = {
            'action' : 'Update',
            'record' : record_id,
            'medical_record' : record,
            'patient': record.patient,
            'sbt' : 'update_medical_record',
            'doctors': Doctor.objects.all(),
        }
        return render(request, 'medical_record_form.html', context)
    return redirect('login')





def delete_medical_record(request, record_id):
    if request.session.get('user'):
        try:
            records = MedicalRecord.objects.get(id=record_id)
            patient_id = records.patient.employee_id
        except MedicalRecord.DoesNotExist:
            return redirect('medical_record') 

        if request.method == 'POST':
            records.delete()
            return redirect('display_medical_record', employee_id=patient_id)

        return render(request, 'delete_medical_record.html', {'record': records})
    return redirect('login')







def search_medical_record(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            try:
                request.session['dates'] = {
                    'begin' : request.POST['begin_date'],
                    'end' : request.POST['end_date']
                }
                return redirect('display_medical_record',employee_id = employee_id)
            except:
                pass
        return redirect('display_medical_record', employee_id = employee_id)
    return redirect('login')






















def back_to_medical_record(request,record_id):
    if request.session.get('user'):
        records = MedicalRecord.objects.filter(id=record_id)
        patient = records.first().patient
        total_price = records.first().price
        context = {'records': records,'patient': patient, 'total_price' : total_price}
        return render(request, 'medical_record.html',context)
    return redirect('login')






from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas

def download_medical_record(request, record_id):
    if request.session.get('user'):
        try:
            medical_record = MedicalRecord.objects.get(id=record_id)
            
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="medical_record.pdf"'
            p = canvas.Canvas(response)
            p.setFont("Helvetica", 12)
            
            p.drawString(100, 700, f"Name: {medical_record.patient.employee_name}")
            p.drawString(100, 680, f"Date: {medical_record.date}")
            p.drawString(100, 660, f"Price: {medical_record.price}")

            p.showPage()
            p.save()

            return response
        except MedicalRecord.DoesNotExist:
            return HttpResponse("Medical Record not found", status=404)
    return redirect('login') 
