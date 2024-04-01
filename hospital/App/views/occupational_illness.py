
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



from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_occupational_illness(request, occupational_illness_id):
    if request.session.get('user'):
        # Retrieve the OccupationalIllness object based on the occupational_illness_id
        occupational_illness = OccupationalIllness.objects.get(id=occupational_illness_id)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="occupational_illness.pdf"'

        # Create the PDF content
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)

        # Write the heading with employee name
        employee_name = occupational_illness.employee_id.employee_name
        p.drawString(50, 750, f"Occupational Illness Information for {employee_name}")

        p.setFont("Helvetica", 12)

        # Write the OccupationalIllness information to the PDF
        p.drawString(50, 720, f"Date: {occupational_illness.date}")
        p.drawString(50, 700, f"Maladie: {occupational_illness.sickness}")
        p.drawString(50, 680, f"Tableau: {occupational_illness.table}")
        p.drawString(50, 660, f"Causal Agent: {occupational_illness.causal_agent}")
        p.drawString(50, 640, f"Job: {occupational_illness.job}")
        p.drawString(50, 620, f"Decision: {occupational_illness.decision}")

        p.showPage()
        p.save()

        return response
    return redirect('login')