from django.shortcuts import render
from App.models import Appointment, Patient

def appointment(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    appointments = Appointment.objects.filter(patient=employee_id)
    context = {'appointments': appointments, 'patient': patient}
    return render(request, 'appointment.html', context)



from django.shortcuts import redirect
from App.models.forms import AppointmentForm
from App.models import Doctor

def add_appointment(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    doctors = Doctor.objects.all()
    context = {'patient': patient, 'doctors': doctors}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment', employee_id=employee_id)
    return render(request, 'add_appointment.html', context)    




def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment', employee_id=appointment.patient.employee_id)

    context = {'appointment': appointment}
    return render(request, 'delete_appointment.html', context)


def change_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment', employee_id=appointment.patient.employee_id)
    else:
        form = AppointmentForm(instance=appointment)

    context = {'form': form, 'appointment': appointment}
    return render(request, 'change_appointment.html', context)
   




