from django.shortcuts import render, get_object_or_404, redirect
from App.models import Doctor
from App.models.forms import DoctorForm

def change_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, doctor_id=doctor_id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor')
    else:
        form = DoctorForm(instance=doctor)

    context = {
        'form': form,
        'doctor': doctor
    }

    return render(request, 'change_doctor.html', context)