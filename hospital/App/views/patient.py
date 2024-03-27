

from django.shortcuts import render, redirect, get_object_or_404
from App.models import Patient,Enterprise
from App.models.forms import PatientForm






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
                return redirect('patient', employee_id = 'all')
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
            return redirect('patient', employee_id = 'all')
        return render(request, 'delete_patient.html', {'patient': patient})
    return redirect('login')




def update_patient(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        if request.method == 'POST':
            form = PatientForm(request.POST, instance=patient)
            if form.is_valid():
                form.save()
                return redirect('patient',employee_id = 'all')  # Redirect to the patient page after successful modification
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