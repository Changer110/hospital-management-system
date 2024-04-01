
from .import_all import *


def display_occupational_illness(request, employee_id):
    if request.session.get('user'):
        context = {
            'patient': Patient.objects.get(employee_id=employee_id),
            'occupational_illnesses': OccupationalIllness.objects.filter(employee_id = employee_id),
        }
        return render(request, 'occupational_illness.html', context)
    return redirect('login')


def add_occupational_illness(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = OccupationalIllnessForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('display_occupational_illness', employee_id = employee_id)
            return redirect('add_occupational_illness', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'value' : employee_id,
            'sbt' : 'add_occupational_illness',
            'patient': Patient.objects.get(employee_id = employee_id)
            }
        return render(request, 'occupational_illness_form.html', context)
    return redirect('login')


def update_occupational_illness(request, occupational_illness_id):
    if request.session.get('user'):
        occupational_illness = OccupationalIllness.objects.get(id = occupational_illness_id) 
        if request.method == 'POST':
            form = OccupationalIllnessForm(request.POST, instance=occupational_illness)
            if form.is_valid():
                form.save()
                return redirect('display_occupational_illness', employee_id = occupational_illness.employee_id.employee_id)
            return redirect('update_occupational_illness', occupational_illness_id = occupational_illness_id)
        context = {
            'action' : 'Update',
            'value' : occupational_illness_id,
            'sbt' : 'update_occupational_illness',
            'patient': occupational_illness.employee_id,
            'occupational_illness' : occupational_illness
            }
        return render(request, 'occupational_illness_form.html', context)
    return redirect('login')



def delete_occupational_illness(request, occupational_illness_id):
    if request.session.get('user'):
        occupational_illness = OccupationalIllness.objects.get(id=occupational_illness_id)
        
        if request.method == 'POST':
            occupational_illness.delete()
            return redirect('occupational_illness',employee_id=occupational_illness.employee_id.employee_id)
        
        context = {'occupational_illness': occupational_illness}
        return render(request, 'delete_occupational_illness.html', context)
    return redirect('login')