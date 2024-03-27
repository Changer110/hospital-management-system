from django.shortcuts import render,redirect
from App.models import Doctor
from App.models.forms import DoctorForm

def display_doctors(request):
    if request.session.get('user'):
        doctors = Doctor.objects.all()
        context = {'doctors': doctors}
        return render(request, 'doctor.html', context)
    return redirect('login')


def add_doctor(request):
    if request.session.get('user'):
        if request.method == 'POST':
            form = DoctorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('doctor')  # Redirect to the doctor list page
        else:
            form = DoctorForm()
        
        context = {'form': form}
        return render(request, 'add_doctor.html', context)
    return redirect('login')


def search_doctor(request):
    if request.session.get('user'):
        if request.method == 'POST':
            doctor_id = request.POST.get('doctor_id')
            doctors = Doctor.objects.filter(doctor_id=doctor_id)
            return render(request, 'doctor.html', {'doctors': doctors})
        return render(request, 'doctor.html', {'doctors': None})
    return redirect('login')


def show_all_doctors(request):
    if request.session.get('user'):
        doctors = Doctor.objects.all()
        return render(request, 'doctor.html', {'doctors': doctors})
    return redirect('login')
    