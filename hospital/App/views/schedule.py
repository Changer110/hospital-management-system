
from .import_all import *



def display_schedule(request, doctor_id):
    if request.session.get('user'):
        doctor = Doctor.objects.get(doctor_id = doctor_id)
        schedules = Schedule.objects.filter(doctor = doctor_id)
        context = {
            'doctor' : doctor,
            'schedules': schedules
        }
        return render(request, 'schedule.html', context)
    return redirect('login')



def add_schedule(request, doctor_id):
    if request.session.get('user'):
        doctor = Doctor.objects.get(doctor_id = doctor_id)
        if request.method == 'POST':
            form = ScheduleForm(request.POST)
            if form.is_valid():
                schedule = form.save()
                request.session['schedule_id'] = schedule.pk
                return redirect('display_schedule', doctor_id = doctor_id)
            return redirect('add_schedule', doctor_id = doctor_id)
        context = {
            'action' : 'Add',
            'doctor' : doctor,
            'value' : doctor_id,
            'sbt' : 'add_schedule'
            }
        return render(request, 'schedule_form.html', context)
    return redirect('login')




def update_schedule(request, schedule_id):
    if request.session.get('user'):
        schedule = Schedule.objects.get(pk = schedule_id)
        if request.method == 'POST':
            form = ScheduleForm(request.POST, instance = schedule)
            if form.is_valid():
                form.save()
                return redirect('display_schedule', doctor_id = schedule.doctor.doctor_id)
            return redirect('update_schedule', schedule_id = schedule_id)
        context = {
            'action' : 'Update',
            'sbt' : 'update_schedule',
            'value' : schedule.pk,
            'schedule' : schedule,
            'doctor' : schedule.doctor
        }
        return render(request, 'schedule_form.html', context)
    return redirect('login')

def delete_schedule(request):
    return