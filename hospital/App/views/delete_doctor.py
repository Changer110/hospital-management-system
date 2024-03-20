from django.shortcuts import render, redirect
from App.models import Doctor

def delete_doctor(request, doctor_id):
    if request.session.get('user'):
        doctor = Doctor.objects.get(doctor_id=doctor_id)
        
        if request.method == 'POST':
            doctor.delete()
            return redirect('doctor_list')  # Redirect to the doctor list page after deletion
        
        context = {
            'doctor': doctor
        }
        
        return render(request, 'delete_doctor.html', context)
    return redirect('login')