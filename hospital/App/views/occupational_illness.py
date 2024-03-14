from django.shortcuts import render,redirect
from App.models import OccupationalIllness, Patient

def display_occupational_illness(request, employee_id):

  patient = Patient.objects.get(employee_id=employee_id)
  occupational_illnesses = OccupationalIllness.objects.filter(employee_id=employee_id)
  context = {'occupational_illnesses': occupational_illnesses, 'patient': patient}
  return render(request, 'occupational_illness.html', context)


from App.models.forms import OccupationalIllnessForm

def add_occupational_illness(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    context = {'patient': patient}
    
    if request.method == 'POST':
        form = OccupationalIllnessForm(request.POST)
        
        if form.is_valid():
            occupational_illness = form.save(commit=False)
            occupational_illness.patient = patient
            occupational_illness.save()
            return redirect('occupational_illness', employee_id=employee_id)
    
    else:
        form = OccupationalIllnessForm()
    
    context['form'] = form
    return render(request, 'add_occupational_illness.html', context)


def change_occupational_illness(request, occupational_illness_id):
    occupational_illness = OccupationalIllness.objects.get(id=occupational_illness_id) 

    if request.method == 'POST':
        form = OccupationalIllnessForm(request.POST, instance=occupational_illness)
        if form.is_valid():
            form.save()
            return redirect('occupational_illness', employee_id=occupational_illness.employee_id.employee_id)
    else:
        form = OccupationalIllnessForm(instance=occupational_illness)

    context = {'form': form, 'occupational_illness': occupational_illness}
    return render(request, 'change_occupational_illness.html', context)



def delete_occupational_illness(request, occupational_illness_id):
    occupational_illness = OccupationalIllness.objects.get(id=occupational_illness_id)
    
    if request.method == 'POST':
        occupational_illness.delete()
        return redirect('occupational_illness',employee_id=occupational_illness.employee_id.employee_id)
    
    context = {'occupational_illness': occupational_illness}
    return render(request, 'delete_occupational_illness.html', context)