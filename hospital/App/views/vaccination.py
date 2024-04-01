from django.shortcuts import render,redirect
from App.models import  Vaccination, MedicalRecord
from App.models.forms import VaccinationForm


def display_vaccination(request, medical_record_id):
    if request.session.get('user'):
        vaccinations = Vaccination.objects.filter(medical_record=medical_record_id)
        context = {'vaccinations': vaccinations, 'record': medical_record_id}
        return render(request, 'vaccination.html', context)
    return redirect('login')



def add_vaccination(request, medical_record_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = VaccinationForm(request.POST)
            if form.is_valid():
                vaccination = form.save(commit=False)
                vaccination.medical_record_id = medical_record_id
                vaccination.save()
                return redirect('vaccination', medical_record_id=medical_record_id)
        else:
            form = VaccinationForm()
        
        context = {'form': form, 'record': medical_record_id}
        return render(request, 'add_vaccination.html', context)
    return redirect('login')



def delete_vaccination(request, vaccination_id):
    if request.session.get('user'):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
        except Vaccination.DoesNotExist:
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        if request.method == 'POST':
            vaccination.delete()
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        context = {'vaccination': vaccination}
        return render(request, 'delete_vaccination.html', context)
    return redirect('login')


def change_vaccination(request, vaccination_id):
    if request.session.get('user'):
        try:
            vaccination = Vaccination.objects.get(id=vaccination_id)
        except Vaccination.DoesNotExist:
            return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        
        if request.method == 'POST':
            form = VaccinationForm(request.POST, instance=vaccination)
            if form.is_valid():
                form.save()
                return redirect('vaccination', medical_record_id=vaccination.medical_record_id)
        else:
            form = VaccinationForm(instance=vaccination)
        
        context = {'form': form, 'vaccination': vaccination}
        return render(request, 'change_vaccination.html', context)
    return redirect('login')