

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
            return redirect('patient')
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






