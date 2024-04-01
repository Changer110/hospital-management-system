
from .import_all import *


def display_absenteeism(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        absenteeisms = Absenteeism.objects.filter(employee_id=employee_id)
        absenteeism_id = request.session.get('absenteeism_id')
        if absenteeism_id:
            absenteeisms = Absenteeism.objects.filter(pk = absenteeism_id)
            request.session['absenteeism_id'] = None
        context = {
            'absenteeisms' : absenteeisms,
            'patient' : patient
        }
        return render(request, 'absenteeism.html', context)
    return redirect('login')



def add_absenteeism(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)        
        if request.method == 'POST':
            form = AbsenteeismForm(request.POST)
            if form.is_valid():
                absenteeism = form.save()
                request.session['absenteeism_id'] = absenteeism.pk
                return redirect('display_absenteeism', employee_id = employee_id)
            return redirect('add_absenteeism', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'patient' : patient,
            'value' : employee_id,
            'sbt' : 'add_absenteeism',
        }
        return render(request, 'absenteeism_form.html', context)
    return redirect('login')
    


def update_absenteeism(request, absenteeism_id):
    if request.session.get('user'):
        absenteeism = Absenteeism.objects.get(pk = absenteeism_id)
        if request.method == 'POST':
            form = AbsenteeismForm(request.POST, instance = absenteeism)
            if form.is_valid():
                form.save()
                request.session['absenteeism_id'] = absenteeism.pk
                return redirect('display_absenteeism', employee_id = absenteeism.employee_id.employee_id)
            return redirect('update_absenteeism', absenteeism_id = absenteeism_id)
        context = {
            'action' : 'Update',
            'value' : absenteeism_id,
            'absenteeism' : absenteeism,
            'sbt' : 'update_absenteeism',
            'patient' : absenteeism.employee_id
        }
        
        return render(request, 'absenteeism_form.html', context)
    return redirect('login')



def delete_absenteeism(request, absenteeism_id):
    if request.session.get('user'):
        absenteeism = Absenteeism.objects.get(id=absenteeism_id)

        if request.method == 'POST':
            absenteeism.delete()
            return redirect('absenteeism' ,employee_id=absenteeism.employee_id.employee_id )  # Replace 'absenteeism_list' with the appropriate URL pattern name for the absenteeism list view

        context = {'absenteeism': absenteeism}
        return render(request, 'delete_absenteeism.html', context)
    return redirect('login')


def download_absenteeism(request, absenteeism_id):
    if request.session.get('user'):
        absenteeism = Absenteeism.objects.get(id=absenteeism_id)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="absenteeism.pdf"'
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)
        employee_name = absenteeism.employee_id.employee_name
        p.drawString(50, 750, f"Absenteeism Information for {employee_name}")
        p.setFont("Helvetica", 12)
        p.drawString(50, 720, f"Type: {absenteeism.type}")
        p.drawString(50, 700, f"Cause: {absenteeism.cause}")
        p.drawString(50, 680, f"Beginning: {absenteeism.beginning}")
        p.drawString(50, 660, f"Reprise: {absenteeism.reprise}")
        p.drawString(50, 640, f"Days Off: {absenteeism.days_off}")

        p.showPage()
        p.save()

        return response
    return redirect('login')
