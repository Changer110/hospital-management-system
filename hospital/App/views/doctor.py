

from .import_all import *



def display_doctor(request):
    if request.session.get('user'):
        doctors = Doctor.objects.all()
        doctor_id = request.session.get('doctor_id')
        if doctor_id:
            doctors = Doctor.objects.filter(doctor_id = doctor_id)
            request.session['doctor_id'] = None
        elif request.method == 'POST':
            request.session['doctor_id'] = request.POST['doctor_id']
            return redirect('display_doctor')
        context = {'doctors': doctors}
        return render(request, 'doctor.html', context)
    return redirect('login')



def add_doctor(request, doctor_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = DoctorForm(request.POST)
            if form.is_valid():
                doctor = form.save()
                request.session['doctor_id'] = doctor.doctor_id
                return redirect('display_doctor')
            return redirect('add_doctor', doctor_id = doctor_id)
        context = {
            'action': 'Add',
            'sbt' : 'add_doctor',
            'value' : doctor_id
            }
        return render(request, 'doctor_form.html', context)
    return redirect('login')




def update_doctor(request, doctor_id):
    if request.session.get('user'):
        doctor = Doctor.objects.get(doctor_id = doctor_id)
        if request.method == 'POST':
            form = DoctorForm(request.POST, instance = doctor)
            if form.is_valid():
                form.save()
                return redirect('display_doctor')
            return redirect('update_doctor', doctor_id = doctor_id)
        context = {
            'action' : 'Update',
            'doctor' : doctor,
            'value' : doctor_id,
            'sbt' : 'update_doctor',            
        }

        return render(request, 'doctor_form.html', context)
    return redirect('login')




def delete_doctor(request, doctor_id):
    if request.session.get('user'):
        doctor = Doctor.objects.get(doctor_id=doctor_id)
        
        if request.method == 'POST':
            doctor.delete()
            return redirect('doctor_list')
        
        context = {
            'doctor': doctor
        }
        return render(request, 'delete_doctor.html', context)
    return redirect('login')

 