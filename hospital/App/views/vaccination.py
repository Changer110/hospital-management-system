
from .import_all import *


def display_vaccination(request, medical_record_id):
    if request.session.get('user'):
        record = MedicalRecord.objects.get(pk = medical_record_id)
        vaccinations = Vaccination.objects.filter(medical_record=medical_record_id)
        context = {
            'patient' : record.patient,
            'vaccinations': vaccinations,
            'record': medical_record_id
        }
        return render(request, 'vaccination.html', context)
    return redirect('login')



def add_vaccination(request, medical_record_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = VaccinationForm(request.POST)
            if form.is_valid():
                vaccination = form.save(commit=False)
                vaccination.medical_record_id = medical_record_id
                vaccination.save()
                return redirect('display_vaccination', medical_record_id=medical_record_id)
        context = {
            'action' : 'Add',
            'sbt' : 'add_vaccination',
            'value' : medical_record_id,
            'record' : medical_record_id,
            }
        
        return render(request, 'vaccination_form.html', context)
    return redirect('login')




def update_vaccination(request, vaccination_id):
    if request.session.get('user'):
        
        vaccination = Vaccination.objects.get(id=vaccination_id)
        if request.method == 'POST':
            form = VaccinationForm(request.POST, instance=vaccination)
            if form.is_valid():
                form.save()
                return redirect('display_vaccination', medical_record_id = vaccination.medical_record.pk)
            return redirect('update_vaccination', vaccination_id = vaccination_id)
        context = {
            'action' : 'Update',
            'sbt' : 'update_vaccination',
            'value' : vaccination.pk,
            'record' : vaccination.medical_record.pk,
            'vaccination' : vaccination
            }
        
        return render(request, 'vaccination_form.html', context)
    return redirect('login')


from django.http import Http404

def delete_vaccination(request, vaccination_id):
    if request.session.get('user'):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
            medical_record_id = vaccination.medical_record_id
            if request.method == 'POST':
                vaccination.delete()
                return redirect('display_vaccination', medical_record_id=medical_record_id)
        except Vaccination.DoesNotExist:
            raise Http404("Vaccination does not exist.")
        
        context = {'vaccination': vaccination}
        return render(request, 'delete_vaccination.html', context)
    return redirect('login')







from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_vaccination(request, vaccination_id):
    if request.session.get('user'):
        vaccinations = Vaccination.objects.filter(id=vaccination_id)
        patient = vaccinations.first().medical_record.patient  # Assuming 'patient_name' is a field in the MedicalRecord model
        
        # Create the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=vaccination_{patient.employee_name}.pdf'
        
        # Generate the PDF content using reportlab
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        
        # Write vaccination information in PDF
        p.drawString(100, 700, f"Vaccination Information for {patient.employee_name}")
        p.drawString(100, 675, "------------------------------------")
        y = 650  # Starting y-coordinate for vaccination details
        for vaccination in vaccinations:
            p.drawString(100, y, f"Date: {vaccination.date.strftime('%Y-%m-%d')}")
            p.drawString(100, y - 25, f"Vaccine: {vaccination.vaccine}")
            p.drawString(100, y - 50, f"Lot: {vaccination.lot}")
            p.drawString(100, y - 75, f"Type: {vaccination.type}")
            p.drawString(100, y - 100, f"Dose: {vaccination.dose}")
            p.drawString(100, y - 125, "------------------------------------")
            y -= 150
        
        p.save()
        
        return response
    
    return redirect('login')