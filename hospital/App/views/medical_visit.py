

from django.shortcuts import render, redirect
from App.models import *
from App.models.forms import medicalVisitForm



from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from io import BytesIO
# import json



def show_medical_visit(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        medical_visits = MedicalVisit.objects.filter(employee_id = employee_id)
        context = {'visits': medical_visits, 'patient': patient}
        return render(request, 'medical_visit.html', context)
    return redirect('login')


def add_medical_visit(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        doctors = Doctor.objects.all()
        context = {'patient': patient, 'doctors': doctors}
        if request.method == 'POST':
            form = medicalVisitForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('medical_visit', employee_id=employee_id)
        return render(request, 'medical_visit_form.html', context)
    return redirect('login')




def download_medical_visit(request, visit_id):
    if request.session.get('user'):
        medical_visit = MedicalVisit.objects.get(pk = visit_id)

        titles = [
            'Code : ', 'Medical visit : ','Name : ', 'Gender : ', 'Age : ','Work post : ','Plaintes : ',
            'Poids : ','Size : ','TA : ','PIT : ','PTE : ','PA : ','Pouls : ','AV/OD : ','OG :','Biology : ',
            'Electrocardiogram : ', 'Audiometry : ', 'Spirometry : ', 'RX pulmonery : ','What to do : ','Aptitude : ',
            'Doctor : ']
        
        values = [
            str(medical_visit.employee_id.employee_id),
            medical_visit.hospital_visit,
            medical_visit.employee_id.name,
            medical_visit.employee_id.gender,
            str(medical_visit.employee_id.age),
            medical_visit.plaintes,
            medical_visit.plaintes,
            str(medical_visit.mensuration_kg),
            str(medical_visit.mensuration_size),
            str(medical_visit.mensuration_TA),
            str(medical_visit.mensuration_PIT),
            str(medical_visit.mensuration_PTE),
            str(medical_visit.mensuration_PA),
            str(medical_visit.mensuration_Pouls),
            str(medical_visit.mensuration_AV_OD),
            str(medical_visit.mensuration_OG),
            medical_visit.biology,
            medical_visit.electrocardiogram,
            medical_visit.audiometry,
            medical_visit.spirometry,
            str(medical_visit.RX_pulmonery),
            medical_visit.what_to_do,
            medical_visit.aptitude,
            medical_visit.doctor.name,
        ]

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        p.setFont('Helvetica', 12)
        y = 800 
        for title, value in zip(titles, values):
            p.drawString(100, y, title)
            p.drawString(200, y, value)
            y -= 20

        p.showPage()
        p.save()
        buffer.seek(0)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="medical_visit.pdf"'
        response.write(buffer.read())
        buffer.close()

        return response
    return redirect('login')











def update_medical_visit(request,visit_id):
    if request.session.get('user'):
        try:
            medical_visit = MedicalVisit.objects.get(id=visit_id)
        except :
            return redirect('medical_visit')  # Redirect to medical_record page if record doesn't exist
        if request.method == 'POST':
            form =medicalVisitForm(request.POST, instance=medical_visit)
            if form.is_valid():
                form.save()
                return redirect('medical_visit', employee_id =medical_visit.employee_id.employee_id)
        else:
            form = medicalVisitForm(instance=medical_visit)

        return render(request, 'medical_visit_form.html', {'form': form, 'medical_visit': medical_visit})
    return redirect('login')


def delete_medical_visit(request, visit_id):
    if request.session.get('user'):
        try:
            medical_visit = MedicalVisit.objects.get(id=visit_id)
        except MedicalVisit.DoesNotExist:
            return redirect('medical_visit')  # Redirect to medical_visit list view if record doesn't exist

        if request.method == 'POST':
            medical_visit.delete()
            return redirect('medical_visit', employee_id=medical_visit.employee_id.employee_id)  # Replace 'medical_visit' with the appropriate URL pattern name for the medical visit list view

        context = {'medical_visit': medical_visit}
        return render(request, 'delete_medical_visit.html', context)
    return redirect('login')
