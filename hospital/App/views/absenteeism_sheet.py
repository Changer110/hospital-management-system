from django.shortcuts import render, redirect
from App.models import Absenteeism,Patient
from App.models.forms import AbsenteeismForm

def absenteeism(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    absenteeisms = Absenteeism.objects.filter(employee_id=employee_id)
    context = {'absenteeisms': absenteeisms,'patient': patient}
    return render(request, 'absenteeism.html', context)



def add_absenteeism(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    context = {'patient': patient}
    
    if request.method == 'POST':
        form = AbsenteeismForm(request.POST)
        if form.is_valid():
            absenteeism = form.save(commit=False)
            absenteeism.patient = patient
            absenteeism.save()
            return redirect('absenteeism', employee_id=employee_id)  # Replace 'accident' with the appropriate URL pattern name for the accident detail view
    else:
        form = AbsenteeismForm()
    
    context['form'] = form

    return render(request, 'add_absenteeism.html', context)


def change_absenteeism(request, absenteeism_id):
    absenteeism = Absenteeism.objects.get(id=absenteeism_id)
    
    if request.method == 'POST':
        form = AbsenteeismForm(request.POST, instance=absenteeism)
        if form.is_valid():
            form.save()
            return redirect('absenteeism', employee_id=absenteeism.employee_id.employee_id)  # Replace 'absenteeism' with the appropriate URL pattern name for the absenteeism detail view
    else:
        form = AbsenteeismForm(instance=absenteeism)
    
    context = {'form': form, 'absenteeism': absenteeism}
    return render(request, 'change_absenteeism.html', context)



def delete_absenteeism(request, absenteeism_id):
    absenteeism = Absenteeism.objects.get(id=absenteeism_id)

    if request.method == 'POST':
        absenteeism.delete()
        return redirect('absenteeism' ,employee_id=absenteeism.employee_id.employee_id )  # Replace 'absenteeism_list' with the appropriate URL pattern name for the absenteeism list view

    context = {'absenteeism': absenteeism}
    return render(request, 'delete_absenteeism.html', context)
