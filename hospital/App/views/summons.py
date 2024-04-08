

from .import_all import *



def display_summons(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        summonses = Summons.objects.filter(employee_id = employee_id)
        summons_id = request.session.get('summons_id')
        if summons_id:
            summonses = Summons.objects.filter(id = summons_id)
            request.session['summons_id'] = None
        context = {
            'patient' : patient,
            'summonses' : summonses
            }
        return render(request, 'summons.html', context)
    return redirect('login')



def add_summons(request, employee_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = SummonsForm(request.POST)
            if form.is_valid():
                summons = form.save()
                request.session['summons_id'] = summons.pk
                return redirect('display_summons', employee_id = employee_id)
            return redirect('add_summons', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'sbt' : 'add_summons',
            'value' : employee_id,
            'patient' : Patient.objects.get(employee_id = employee_id),
        }
        return render(request, 'summons_form.html', context)
    return redirect('login')



def update_summons(request, summons_id):
    if request.session.get('user'):
        summons = Summons.objects.get(id = summons_id)
        if request.method == 'POST':
            form = SummonsForm(request.POST, instance = summons)
            if form.is_valid():
                form.save()
                request.session['summons_id'] = summons_id
                return redirect('display_summons', employee_id = summons.employee_id.employee_id)
            return redirect('update_summons', summons_id = summons_id)
        context = {
            'action' : 'Update',
            'summons' : summons,
            'value' : summons_id,
            'sbt' : 'update_summons',
            'patient' : summons.employee_id,
        }
        return render(request, 'summons_form.html', context)
    return redirect('login')



def delete_summons(request, summons_id):
    if request.session.get('user'):
        summons_form = Summons.objects.get(id=summons_id)
        if request.method == 'POST':
            summons_form.delete()
            return redirect('display_summons',employee_id=summons_form.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'summons_form': summons_form}
        return render(request, 'delete_summons_form.html', context)
    return redirect('login')



def download_summons(request, summons_id):
    summons = Summons.objects.get(id=summons_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="summons.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)
    employee_name = summons.employee_id.employee_name
    p.drawString(50, 750, f"Summons Form for {employee_name}")
    p.setFont("Helvetica", 12)
    p.drawString(50, 720, f"Motif: {summons.motif}")
    p.drawString(50, 700, f"Date of Issue: {summons.issue_date}")
    p.drawString(50, 680, f"Date of Summons: {summons.summons_date}")
    p.drawString(50, 660, f"Date de Presentation: {summons.presentation_date}")
    p.drawString(50, 640, f"Observation: {summons.observation}")

    p.showPage()
    p.save()

    return response