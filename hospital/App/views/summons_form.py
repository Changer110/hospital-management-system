from django.shortcuts import render,redirect
from App.models import SummonsForm, Patient






def display_summons_form(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        summons_forms = SummonsForm.objects.filter(employee_id=employee_id)
        context = {'summons_forms': summons_forms, 'patient': patient}
        return render(request, 'summons_form.html', context)
    return redirect('login')




from App.models.forms import SummonsFormForm

def add_summons_form(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        context = {'patient': patient}
        if request.method == 'POST':
            form = SummonsFormForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('summons_form', employee_id=employee_id)
        return render(request, 'add_summons_form.html', context)
    return redirect('login')



def change_summons_form(request, summons_form_id):
    if request.session.get('user'):
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
    return redirect('login')


def delete_summons_form(request, summons_form_id):
    if request.session.get('user'):
        summons_form = SummonsForm.objects.get(id=summons_form_id)
        if request.method == 'POST':
            summons_form.delete()
            return redirect('summons_form',employee_id=summons_form.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'summons_form': summons_form}
        return render(request, 'delete_summons_form.html', context)
    return redirect('login')



from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_summons_form(request, summons_form_id):
    # Retrieve the SummonsForm object based on the summons_form_id
    summons_form = SummonsForm.objects.get(id=summons_form_id)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="summons_form.pdf"'

    # Create the PDF content
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)

    # Write the heading with employee name
    employee_name = summons_form.employee_id.name
    p.drawString(50, 750, f"Summons Form for {employee_name}")

    p.setFont("Helvetica", 12)

    # Write the SummonsForm information to the PDF
    p.drawString(50, 720, f"Motif: {summons_form.motif}")
    p.drawString(50, 700, f"Date of Issue: {summons_form.date_of_issue}")
    p.drawString(50, 680, f"Date of Summons: {summons_form.date_of_summons}")
    p.drawString(50, 660, f"Date de Presentation: {summons_form.date_de_presentation}")
    p.drawString(50, 640, f"Observation: {summons_form.observation}")

    p.showPage()
    p.save()

    return response