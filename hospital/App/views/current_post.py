


from django.shortcuts import render, redirect
from App.models.forms import CurrentPostForm
from App.models import *





def display_current_post(request, employee_id):
    posts = CurrentPost.objects.filter(employee_id = employee_id)
    context = {'posts' : posts, 'patient' : Patient.objects.get(employee_id = employee_id)}
    return render(request, 'current_post.html', context)



def add_current_post(request, employee_id):
    if request.method == 'POST':
        form = CurrentPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_current_post', employee_id = employee_id)
    context = {
        'action' : 'Add',
        'sbt' : 'add_current_post',
        'value' : employee_id,
        'patient' : Patient.objects.get(employee_id = employee_id)
    }
    return render(request, 'current_post_form.html', context)



def update_current_post(request, current_post_id):
    if request.session.get('user'):
        current_post = CurrentPost.objects.get(id=current_post_id)
        if request.method == 'POST':
            form = CurrentPostForm(request.POST, instance=current_post)
            if form.is_valid():
                form.save()
                return redirect('display_current_post', employee_id=current_post.employee_id.employee_id)
            return redirect('update_current_post', current_post_id = current_post_id)
        context = {
            'action' : 'Update',
            'sbt' : 'update_current_post',
            'value' : current_post_id,
            'current_post' : current_post,
            'patient' : current_post.employee_id
        }
        return render(request, 'current_post_form.html', context)
    return redirect('login')



def delete_current_post(request, current_post_id):
    if request.session.get('user'):
        current_post = CurrentPost.objects.get(id=current_post_id)

        if request.method == 'POST':
            current_post.delete()
            return redirect('current_post', employee_id=current_post.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'current_post': current_post}
        return render(request, 'delete_current_post.html', context)
    return redirect('login') 



from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_current_post(request, current_post_id):
    if request.session.get('user'):
        # Retrieve the CurrentPost object based on the current_post_id
        current_post = CurrentPost.objects.get(id=current_post_id)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="current_post.pdf"'

        # Create the PDF content
        p = canvas.Canvas(response)
        p.setFont("Helvetica-Bold", 16)

        # Write the heading with employee name
        employee_name = current_post.employee_id.name
        p.drawString(50, 750, f"Current Post Information for {employee_name}")

        p.setFont("Helvetica", 12)

        # Write the CurrentPost information to the PDF
        p.drawString(50, 720, f"Begin Date: {current_post.begin_date}")
        p.drawString(50, 700, f"End Date: {current_post.end_date}")
        p.drawString(50, 680, f"Post: {current_post.post}")
        p.drawString(50, 660, f"Tasks: {current_post.tasks}")
        p.drawString(50, 640, f"Work Rate: {current_post.work_rate}")
        p.drawString(50, 620, f"Nuisance Factors: {current_post.nusance_factors}")
        p.drawString(50, 600, f"Metrology Date: {current_post.metrology_date}")
        p.drawString(50, 580, f"Metrology Type: {current_post.metrology_type}")
        p.drawString(50, 560, f"Metrology R: {current_post.metrology_R}")

        p.showPage()
        p.save()

        return response
    return redirect('login')