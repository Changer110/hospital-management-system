

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



def download_accident(request, accident_id):
    if request.session.get('user'):
        # Retrieve the Accident object based on the accident_id
        accident = Accident.objects.get(id=accident_id)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="accident.pdf"'

        # Create the PDF content
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)

        # Write the heading with employee name
        employee_name = accident.employee_id.employee_name
        p.drawString(50, 750, f"Accident Information for {employee_name}")

        p.setFont("Helvetica", 12)

        # Write the Accident information to the PDF
        p.drawString(50, 720, f"Date: {accident.date}")
        p.drawString(50, 700, f"Causal Material Element: {accident.material_causel}")
        p.drawString(50, 680, f"Nature of Lesions: {accident.lesions_nature}")
        p.drawString(50, 660, f"Position: {accident.position}")
        p.drawString(50, 640, f"Number of Days Off: {accident.days_off}")
        p.drawString(50, 620, f"Partial Permanent Incapacity: {accident.partial_incapacity}")
        p.drawString(50, 600, f"Observation: {accident.observation}")

        p.showPage()
        p.save()

        return response
    return redirect('login')