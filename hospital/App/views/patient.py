

from .import_all import *


def display_patient(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            employee_id = request.POST.get('employee_id')
            return redirect('display_patient', employee_id = employee_id)
        try:
            patients = Patient.objects.filter(employee_id = int(employee_id))
        except:
            patients = Patient.objects.all()
        context = {'patients': patients}
        return render(request, 'patient.html', context)
    return redirect('login')




def add_patient(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            pic = request.FILES['picture']
            img_file = os.path.join(settings.BASE_DIR, 'App/static/img', pic.name)
            with open(img_file, 'wb+') as file:
                for chunk in pic.chunks():
                    file.write(chunk)
            form = PatientForm(request.POST)
            if form.is_valid():
                patient = form.save(commit=False)
                patient.picture = pic.name
                patient.creation_date = date_time_now()
                patient.save()
                return redirect('patient', employee_id = patient.employee_id)
        context = {
            'action' : 'Add',
            'sbt' : 'add_patient', 
            'employee' : employee_id,
            'enterprises': Enterprise.objects.all()
        }
        return render(request, 'patient_form.html', context)
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
        db_patient = Patient.objects.get(employee_id=employee_id)
        if request.method == 'POST':
            pic = request.FILES.get('picture')
            if pic:
                img_file = os.path.join(settings.BASE_DIR, 'App/static/img', pic.name)
                with open(img_file, 'wb+') as file:
                    for chunk in pic.chunks():
                        file.write(chunk)
            form = PatientForm(request.POST, instance = db_patient)
            if form.is_valid():
                patient = form.save(commit=False)
                patient.picture = pic.name if pic else db_patient.picture
                patient.save()
                return redirect('patient', employee_id = patient.employee_id)
            return redirect('change_patient', employee_id = db_patient.employee_id)
        context = {
            'action' : 'Update',
            'patient' : db_patient,
            'employee' : employee_id,
            'sbt' : 'change_patient',
            'enterprises' : Enterprise.objects.all(),            
            }
        return render(request, 'patient_form.html', context)
    return redirect('login')








def download_patient(request, employee_id):
    if request.session.get('user'):
        try:
            patient = Patient.objects.get(employee_id=employee_id)
        except Patient.DoesNotExist:
            return HttpResponse("Patient not found.", status=404)
        
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        p.setFont("Helvetica", 10)
        heading_color = "#004d99"
        content_color = "#333333"
        p.setFont("Helvetica-Bold", 16)
        p.setFillColor(heading_color)
        p.drawString(100, 750, "Patient Data")

        p.setFont("Helvetica-Bold", 12)
        y = 700
        row_height = 20
        data = [
            f"Employee ID: {patient.employee_id}",
            f"Name: {patient.employee_name}",
            f"Patient Creation Date: {patient.creation_date}",
            f"Enterprise Name: {patient.enterprise_ID.name}",
            f"Date of Birth: {patient.birth_date}",
            f"Place of Birth: {patient.birth_date}",
            f"Nationality: {patient.nationality}",
            f"Age: {patient.age}",
            f"Gender: {patient.gender}",
            f"Phone Number: {patient.phone_number}",
            f"Email: {patient.email}",
            f"Address: {patient.address}",
            f"Size: {patient.size}",
            f"Blood Group: {patient.blood_group}",
            f"Marital Status: {patient.marital_status}",
            f"Number of Dependent Children: {patient.dependent_children}",
            f"Affiliation with INSS: {patient.affiliation_with_inss}",
            f"Emergency Contact: {patient.emergency_contact}",
            f"Hiring Date: {patient.hiring_date}",
            f"Departure Date: {patient.departure_date}",
            f"Reason for Leaving: {patient.leaving_reason}",
            f"Qualification: {patient.qualification}",
            # Add more fields as needed
        ]
        for item in data:
            p.setFillColor(content_color)
            p.drawString(150, y, item)
            y -= row_height

        if patient.picture:
            image_path = os.path.join(settings.BASE_DIR, 'App/static/img', str(patient.picture))
            if os.path.exists(image_path):
                image = PILImage.open(image_path)
                max_image_width = 500
                max_image_height = 150
                image.thumbnail((max_image_width, max_image_height))
                image_width, image_height = image.size
                p.drawInlineImage(image_path, 400, 650, width=image_width, height=image_height)

        p.showPage()
        p.save()

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="patient_{employee_id}_data.pdf"'
        return response
    
    return redirect('login')