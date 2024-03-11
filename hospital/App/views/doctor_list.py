from django.shortcuts import render
from App.models.doctor import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, 'doctor_list.html', context)