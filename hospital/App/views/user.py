



from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    page = 'login'
    if request.method == 'POST':
        uname = request.POST['username']
        ukey = request.POST['password']
        user = authenticate(request, username = uname, password = ukey)
        if user:
            login(request, user)
            request.session['user'] = user.pk
            request.session['role'] = user.role
            return redirect('patient', employee_id = 'all')
        return redirect(page)
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request,'index.html')
    #     return redirect(page, employee_id = 'all')
    # return render(request, 'login.html')


# def user_page(request):
#     page = 'login'
#     if request.session.get('user'):
#         return render
#     return redirect([page])



from django.http import HttpResponse
from reportlab.pdfgen import canvas

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
    return redirect('login')







def download_background_patient(request, background_patient_id):
    if request.session.get('user'):
        # Retrieve the background patient object based on the background_patient_id
        background_patient = BackgroundPatient.objects.get(id=background_patient_id)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="background_patient.pdf"'

        # Create the PDF content
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)

        # Write the heading with employee name
        employee_name = background_patient.employee_id.name
        p.drawString(50, 750, f"Background Information for {employee_name}")

        p.setFont("Helvetica", 12)

        # Write the background patient information to the PDF
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


def download_absenteeism(request, absenteeism_id):
    if request.session.get('user'):
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
    return redirect('login')



