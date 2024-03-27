

from django.shortcuts import render, redirect, get_object_or_404
from App.models import Patient,Enterprise
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
            return redirect('patient', employee_id = 'all')
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









def show_all_patient(request):
    patients = Patient.objects.all()
    return render(request, 'patient.html', {'patients': patients})

def patient_information(request, employee_id):
    patients = Patient.objects.filter(employee_id=employee_id)
    context = {'patients': patients}
    return render(request, 'patient.html', context)


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

def download_patient(request, employee_id):
    if request.session.get('user'):
        try:
            patient = Patient.objects.get(employee_id=employee_id)
        except Patient.DoesNotExist:
            return HttpResponse("Patient not found.", status=404)

        # Create a file-like buffer to receive PDF data
        buffer = BytesIO()

        # Create the PDF object, using the buffer as its "file"
        p = canvas.Canvas(buffer, pagesize=letter)

        # Set the font and font size
        p.setFont("Helvetica", 10)

        # Write the title
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, 750, "Patient Data")

        # Write the patient details
        p.setFont("Helvetica-Bold", 12)
        y = 700
        data = [
            f"Employee ID: {patient.employee_id}",
            f"Name: {patient.name}",
            f"Patient Creation Date: {patient.patient_creation_date}",
            f"Enterprise Name: {patient.enterprise_name.enterprise_ID}",
            f"Date of Birth: {patient.date_of_birth}",
            f"Place of Birth: {patient.place_of_birth}",
            f"Nationality: {patient.nationality}",
            f"Age: {patient.age}",
            f"Gender: {patient.gender}",
            f"Phone Number: {patient.phone_number}",
            f"Email: {patient.email}",
            f"Address: {patient.address}",
            f"Size: {patient.size}",
            f"Blood Group: {patient.blood_group}",
            f"Marital Status: {patient.marital_status}",
            f"Number of Dependent Children: {patient.num_dependent_children}",
            f"Affiliation with INSS: {patient.affiliation_with_inss}",
            f"Emergency Contact: {patient.emergency_contact}",
            f"Hiring Date: {patient.hiring_date}",
            f"Departure Date: {patient.departure_date}",
            f"Reason for Leaving: {patient.reason_for_leaving}",
            f"Qualification: {patient.qualification}",
            
            # Add more fields as needed
        ]
        row_height = 20
        for item in data:
            p.drawString(150, y, item)
            y -= row_height

        # Close the PDF object cleanly
        p.showPage()
        p.save()

        # File response with the generated PDF
        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="patient_{employee_id}_data.pdf"'
        return response
    return redirect('login')
def convert_date(value):
    date = parser.parse(Value).strftime("%Y-%m-%d")
    return datetime.strptime(value, "%Y-%m-%d").date()
