from django.shortcuts import render, redirect
from App.models import Accident,Patient
from App.models.forms import AccidentForm

def accident(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        accidents = Accident.objects.filter(employee_id=employee_id)
        context = {'accidents': accidents,'patient': patient}
        return render(request, 'accident.html', context)
    return redirect('login')


def add_accident(request, employee_id):
    if request.session.get('user'):
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
    return redirect('login')



def change_accident(request, accident_id):
    if request.session.get('user'):
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
    return redirect('login')


def delete_accident(request, accident_id):
    if request.session.get('user'):
        accident = Accident.objects.get(id=accident_id)

        if request.method == 'POST':
            accident.delete()
            return redirect('accident',employee_id=accident.employee_id.employee_id)  # Replace 'accident_list' with the appropriate URL pattern name for the accident list view

        context = {'accident': accident}
        return render(request, 'delete_accident.html', context)
    return redirect('login')


from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_accident(request, accident_id):
    # Retrieve the Accident object based on the accident_id
    accident = Accident.objects.get(id=accident_id)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="accident.pdf"'

    # Create the PDF content
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)

    # Write the heading with employee name
    employee_name = accident.employee_id.name
    p.drawString(50, 750, f"Accident Information for {employee_name}")

    p.setFont("Helvetica", 12)

    # Write the Accident information to the PDF
    p.drawString(50, 720, f"Date: {accident.date}")
    p.drawString(50, 700, f"Causal Material Element: {accident.causal_material_element}")
    p.drawString(50, 680, f"Nature of Lesions: {accident.nature_of_lesions}")
    p.drawString(50, 660, f"Position: {accident.position}")
    p.drawString(50, 640, f"Number of Days Off: {accident.numb_of_days_off}")
    p.drawString(50, 620, f"Partial Permanent Incapacity: {accident.partial_permanent_incapacity}")
    p.drawString(50, 600, f"Observation: {accident.observation}")

    p.showPage()
    p.save()

    return response