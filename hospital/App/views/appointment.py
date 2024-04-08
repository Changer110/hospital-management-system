
from .import_all import *


def display_appointment(request, employee_id):
    try:
        patient = Patient.objects.get(employee_id = int(employee_id)).employee_id
        appointment = Appointment.objects.filter(patient = int(employee_id))
        user = 'for '+str(patient.employee_name)
    except:
        user = ''
        patient = 'all'
        appointment = Appointment.objects.all()
    
    context = {
        'appointments' : appointment,
        'user': user,
        'value' : patient
    }
    return render(request, 'appointment.html', context)



def add_appointment(request, employee_id):
    try:
        patient = Patient.objects.get(employee_id = int(employee_id))
    except:
        patient = Patient.objects.all() 
    doctors = Doctor.objects.all()
    context = {
        'action' : 'Add',
        'doctors': doctors,
        'patients': patient, 
        'value' : employee_id,
        'sbt' : 'add_appointment', 
    }
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_appointment', employee_id = employee_id)
        return redirect('add_appointment', employee_id = employee_id)
    return render(request, 'appointment_form.html', context)    




def update_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id = appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance = appointment)
        if form.is_valid():
            form.save()
            return redirect('display_appointment', employee_id = appointment.patient.employee_id)
        return redirect('update_appointment', appointment_id = appointment_id)
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all() 
    context = {
        'doctors': doctors,
        'action' : 'Update',
        'patients': patients,
        'value' : appointment_id,
        'appointment' : appointment,
        'sbt' : 'update_appointment'
    }
    return render(request, 'appointment_form.html', context)




def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment', employee_id=appointment.patient.employee_id)

    context = {'appointment': appointment}
    return render(request, 'delete_appointment.html', context)