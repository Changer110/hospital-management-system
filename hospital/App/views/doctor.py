from django.shortcuts import render
from App.models import Doctor

def display_doctors(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor.html', context)

def search_doctor(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        doctors = Doctor.objects.filter(doctor_id=doctor_id)
        return render(request, 'doctor.html', {'doctors': doctors})
    return render(request, 'doctor.html', {'doctors': None})


def show_all_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})