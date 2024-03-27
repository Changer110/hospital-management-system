from django.shortcuts import render, redirect
from App.models import Absenteeism,Patient
from App.models.forms import AbsenteeismForm

def absenteeism(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        absenteeisms = Absenteeism.objects.filter(employee_id=employee_id)
        context = {'absenteeisms': absenteeisms,'patient': patient}
        return render(request, 'absenteeism.html', context)
    return redirect('login')



def add_absenteeism(request, employee_id):
    if request.session.get('user'):
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
    return redirect('login')
    


def change_absenteeism(request, absenteeism_id):
    if request.session.get('user'):
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


from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_absenteeism(request, absenteeism_id):
    # Retrieve the Absenteeism object based on the absenteeism_id
    absenteeism = Absenteeism.objects.get(id=absenteeism_id)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="absenteeism.pdf"'

    # Create the PDF content
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)

    # Write the heading with employee name
    employee_name = absenteeism.employee_id.name
    p.drawString(50, 750, f"Absenteeism Information for {employee_name}")

    p.setFont("Helvetica", 12)

    # Write the Absenteeism information to the PDF
    p.drawString(50, 720, f"Type: {absenteeism.type}")
    p.drawString(50, 700, f"Cause: {absenteeism.cause}")
    p.drawString(50, 680, f"Beginning: {absenteeism.beginning}")
    p.drawString(50, 660, f"Reprise: {absenteeism.reprise}")
    p.drawString(50, 640, f"Days Off: {absenteeism.days_off}")

    p.showPage()
    p.save()

    return response
