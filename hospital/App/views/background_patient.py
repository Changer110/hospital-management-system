from django.shortcuts import render,redirect
from App.models import BackgroundPatient, Patient


def display_background_patient(request, employee_id):
    if request.session.get('user'):

        patient = Patient.objects.get(employee_id=employee_id)
        background_patients = BackgroundPatient.objects.filter(employee_id=employee_id)
        context = {'background_patients': background_patients, 'patient': patient}
        return render(request, 'background_patient.html', context)
    return redirect('login')



from App.models.forms import BackgroundPatientForm

def add_background_patient(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        context = {'patient': patient}
        if request.method == 'POST':
            form = BackgroundPatientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('background_patient', employee_id=employee_id)
        return render(request, 'add_background_patient.html', context)
    return redirect('login')
  
  
  
  
def change_background_patient(request, background_patient_id):
    if request.session.get('user'):
        background_patient = BackgroundPatient.objects.get(id=background_patient_id)

        if request.method == 'POST':
            form = BackgroundPatientForm(request.POST, instance=background_patient)
            if form.is_valid():
                form.save()
                return redirect('background_patient', employee_id=background_patient.employee_id.employee_id)
        else:
            form = BackgroundPatientForm(instance=background_patient)

        context = {'form': form, ' background_patient':  background_patient}
        return render(request, 'change_background_patient.html', context)
    return redirect('login') 
  
  
def delete_background_patient(request, background_patient_id):
    if request.session.get('user'):
        background_patient  = BackgroundPatient.objects.get(id=background_patient_id)

        if request.method == 'POST':
            background_patient.delete()
            return redirect('background_patient',employee_id=background_patient.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'background_patient': background_patient}
        return render(request, 'delete_background.html', context)
    return redirect('login')  




from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_background_patient(request, background_patient_id):
    if request.session.get('user'):
        # Retrieve the background patient object based on the background_patient_id
        background_patient = BackgroundPatient.objects.get(id=background_patient_id)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="background_patient.pdf"'

        # Create the PDF content
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)

        # Write the heading with employee name
        employee_name = background_patient.employee_id.name
        p.drawString(50, 750, f"Background Information for {employee_name}")

        p.setFont("Helvetica", 12)

        # Write the background patient information to the PDF
        p.drawString(50, 720, f"Personal Medical: {background_patient.personal_medical}")
        p.drawString(50, 700, f"Personal Surgical: {background_patient.personal_surgical}")
        p.drawString(50, 680, f"Professional Medical: {background_patient.proffesional_medical}")
        p.drawString(50, 660, f"Professional Surgical: {background_patient.proffesional_surgical}")
        p.drawString(50, 640, f"Family Medical: {background_patient.family_medical}")
        p.drawString(50, 620, f"Family Surgical: {background_patient.family_surgical}")
        p.drawString(50, 600, f"Social Personal: {background_patient.social_personal}")
        p.drawString(50, 580, f"Social Family: {background_patient.social_family}")

        p.showPage()
        p.save()

        return response
    return redirect('login') 