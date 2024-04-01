from django.shortcuts import render,redirect
from App.models import  Vaccination, MedicalRecord
from App.models.forms import VaccinationForm


def display_vaccination(request, medical_record_id):
    if request.session.get('user'):
        vaccinations = Vaccination.objects.filter(medical_record=medical_record_id)
        context = {'vaccinations': vaccinations, 'record': medical_record_id}
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
                return redirect('vaccination', medical_record_id=medical_record_id)
        else:
            form = VaccinationForm()
        
        context = {'form': form, 'record': medical_record_id}
        return render(request, 'add_vaccination.html', context)
    return redirect('login')



def delete_vaccination(request, vaccination_id):
    if request.session.get('user'):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
        except Vaccination.DoesNotExist:
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        if request.method == 'POST':
            vaccination.delete()
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        context = {'vaccination': vaccination}
        return render(request, 'delete_vaccination.html', context)
    return redirect('login')


def change_vaccination(request, vaccination_id):
    if request.session.get('user'):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
        except Vaccination.DoesNotExist:
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        if request.method == 'POST':
            form = VaccinationForm(request.POST, instance=vaccination)
            if form.is_valid():
                form.save()
                return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        else:
            form = VaccinationForm(instance=vaccination)
        
        context = {'form': form, 'vaccination': vaccination}
        return render(request, 'change_vaccination.html', context)
    return redirect('login')




from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_vaccination(request, vaccination_id):
    if request.session.get('user'):
        vaccinations = Vaccination.objects.filter(id=vaccination_id)
        patient = vaccinations.first().medical_record.patient  # Assuming 'patient_name' is a field in the MedicalRecord model
        
        # Create the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=vaccination_{patient}.pdf'
        
        # Generate the PDF content using reportlab
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        
        # Write vaccination information in PDF
        p.drawString(100, 700, f"Vaccination Information for {patient}")
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