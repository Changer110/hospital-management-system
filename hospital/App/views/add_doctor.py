from django.shortcuts import render, redirect
from App.models.forms import DoctorForm

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