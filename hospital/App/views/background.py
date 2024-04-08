

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
  


def delete_background(request, background_id):
    if request.session.get('user'):
        background_patient  = Background.objects.get(id=background_id)

        if request.method == 'POST':
            background_patient.delete()
            return redirect('display_background',employee_id=background_patient.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'background_patient': background_patient}
        return render(request, 'delete_background.html', context)
    return redirect('login')



def download_background(request, background_id):
    if request.session.get('user'):
        background_patient = Background.objects.get(id=background_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="background_patient.pdf"'
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)
        employee_name = background_patient.employee_id.employee_name
        p.drawString(50, 750, f"Background Information for {employee_name}")

        p.setFont("Helvetica", 12)
        p.drawString(50, 720, f"Personal Medical: {background_patient.personal_medical}")
        p.drawString(50, 700, f"Personal Surgical: {background_patient.personal_surgical}")
        p.drawString(50, 680, f"Professional Medical: {background_patient.proffesional_medical}")
        p.drawString(50, 660, f"Professional Surgical: {background_patient.proffesional_surgical}")
        p.drawString(50, 640, f"Family Medical: {background_patient.family_medical}")
        p.drawString(50, 620, f"Family Surgical: {background_patient.family_surgical}")
        p.drawString(50, 600, f"Social Personal: {background_patient.social_personal}")
        p.drawString(50, 580, f"Social Family: {background_patient.social_family}")

        p.showPage()
        p.save()

        return response
    return redirect('login') 