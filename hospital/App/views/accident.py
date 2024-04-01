

from .import_all import *


def display_accident(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        accidents = Accident.objects.filter(employee_id=employee_id)
        context = {'accidents': accidents,'patient': patient}
        return render(request, 'accident.html', context)
    return redirect('login')



def add_accident(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        if request.method == 'POST':
            form = AccidentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accident', employee_id = employee_id)
            return redirect('add_accident', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'patient' : patient,
            'sbt' : 'add_accident',
            'value' : employee_id,
        }
        return render(request, 'accident_form.html', context)
    return redirect('login')



def update_accident(request, accident_id):
    if request.session.get('user'):
        accident = Accident.objects.get(id = accident_id) 
        if request.method == 'POST':
            form = AccidentForm(request.POST, instance=accident)
            if form.is_valid():
                form.save()
                return redirect('accident', employee_id = accident.employee_id.employee_id)
            return redirect('update_accident', accident_id = accident_id)
        context = {
            'action' : 'Update',
            'patient' : accident.employee_id,
            'sbt' : 'update_accident',
            'value' : accident_id,
            'accident' : accident
        }
        return render(request, 'accident_form.html', context)
    return redirect('login')



def delete_accident(request, accident_id):
    if request.session.get('user'):
        accident = Accident.objects.get(id=accident_id)

        if request.method == 'POST':
            accident.delete()
            return redirect('accident',employee_id = accident.employee_id.employee_id)

        context = {'accident': accident}
        return render(request, 'delete_accident.html', context)
    return redirect('login')