from django.shortcuts import render,redirect
from App.models import SummonsForm, Patient

def summons_form(request, employee_id):

  patient = Patient.objects.get(employee_id=employee_id)
  summons_forms = SummonsForm.objects.filter(employee_id=employee_id)
  context = {'summons_forms': summons_forms, 'patient': patient}
  return render(request, 'summons_form.html', context)




from App.models.forms import SummonsFormForm

def add_summons_form(request, employee_id):
    patient = Patient.objects.get(employee_id=employee_id)
    context = {'patient': patient}
    if request.method == 'POST':
        form = SummonsFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('summons_form', employee_id=employee_id)
    return render(request, 'add_summons_form.html', context)



def change_summons_form(request, summons_form_id):
    summons_form = SummonsForm.objects.get(id=summons_form_id)
    

    if request.method == 'POST':
        form = SummonsFormForm(request.POST, instance=summons_form)
        if form.is_valid():
            form.save()
            return redirect('summons_form', employee_id=summons_form.employee_id.employee_id)
    else:
        form = SummonsFormForm(instance=summons_form)

    context = {'form': form, 'summons_form': summons_form}
    return render(request, 'change_summons_form.html', context)


def delete_summons_form(request, summons_form_id):
    summons_form = SummonsForm.objects.get(id=summons_form_id)

    if request.method == 'POST':
        summons_form.delete()
        return redirect('summons_form',employee_id=summons_form.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

    context = {'summons_form': summons_form}
    return render(request, 'delete_summons_form.html', context) 