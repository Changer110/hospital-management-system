

from .import_all import *


def display_background(request, employee_id):
    if request.session.get('user'):

        patient = Patient.objects.get(employee_id=employee_id)
        backgrounds = Background.objects.filter(employee_id=employee_id)
        context = {'backgrounds': backgrounds, 'patient': patient}
        return render(request, 'background.html', context)
    return redirect('login')




def add_background(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        if request.method == 'POST':
            form = BackgroundForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('display_background', employee_id = employee_id)
            return redirect('add_background', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'patient' : patient,
            'sbt' : 'add_background',
            'value' : employee_id,
        }
        return render(request, 'background_form.html', context)
    return redirect('login')
  
  
  
  
def update_background(request, background_id):
    if request.session.get('user'):
        background = Background.objects.get(id = background_id)
        if request.method == 'POST':
            form = BackgroundForm(request.POST, instance = background)
            if form.is_valid():
                form.save()
                return redirect('display_background', employee_id = background.employee_id.employee_id)
            return redirect('update_background', background_id = background_id)
        context = {
            'action' : 'Update',
            'value' : background_id,
            'background' :  background,
            'sbt' : 'update_background',
            'patient' : background.employee_id,
        }
        return render(request, 'background_form.html', context)
    return redirect('login') 
  


def delete_background(request, background_patient_id):
    if request.session.get('user'):
        background_patient  = Background.objects.get(id=background_patient_id)

        if request.method == 'POST':
            background_patient.delete()
            return redirect('background_patient',employee_id=background_patient.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'background_patient': background_patient}
        return render(request, 'delete_background.html', context)
    return redirect('login')       