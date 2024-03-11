from django.shortcuts import render, redirect
from App.models import Accident,Patient
from App.models.forms import AccidentForm

def accident(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    accidents = Accident.objects.filter(employee_id=employee_id)
    context = {'accidents': accidents,'patient': patient}
    return render(request, 'accident.html', context)


def add_accident(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    context = {'patient': patient}
    
    if request.method == 'POST':
        form = AccidentForm(request.POST)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.patient = patient
            accident.save()
            return redirect('accident', employee_id=employee_id)  # Replace 'accident' with the appropriate URL pattern name for the accident detail view
    else:
        form = AccidentForm()
    
    context['form'] = form

    return render(request, 'add_accident.html', context)



def change_accident(request, accident_id):
    accident = Accident.objects.get(id=accident_id) 

    if request.method == 'POST':
        form = AccidentForm(request.POST, instance=accident)
        if form.is_valid():
            form.save()
            return redirect('accident', employee_id=accident.employee_id.employee_id)
    else:
        form = AccidentForm(instance=accident)

    context = {'form': form, 'accident': accident}
    return render(request, 'change_accident.html', context)


def delete_accident(request, accident_id):
    accident = Accident.objects.get(id=accident_id)

    if request.method == 'POST':
        accident.delete()
        return redirect('accident',employee_id=accident.employee_id.employee_id)  # Replace 'accident_list' with the appropriate URL pattern name for the accident list view

    context = {'accident': accident}
    return render(request, 'delete_accident.html', context)