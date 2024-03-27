from django.shortcuts import render,redirect
from App.models import PreviousPost, Patient



def previous_post(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        previous_posts = PreviousPost.objects.filter(employee_id=employee_id)
        context = {'previous_posts': previous_posts, 'patient': patient}
        return render(request, 'previous_post.html', context)
    return redirect('login')



from App.models.forms import PreviousPostForm

def add_previous_post(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id=employee_id)
        context = {'patient': patient}
        if request.method == 'POST':
            form = PreviousPostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('previous_post', employee_id=employee_id)
        return render(request, 'add_previous_post.html', context)
    return redirect('login')
  
  
  
def change_previous_post(request, previous_post_id):
    if request.session.get('user'):
        previous_post = PreviousPost.objects.get(id=previous_post_id)
        if request.method == 'POST':
            form = PreviousPostForm(request.POST, instance=previous_post)
            if form.is_valid():
                form.save()
                return redirect('previous_post', employee_id=previous_post.employee_id.employee_id)
        else:
            form = PreviousPostForm(instance=previous_post)
        context = {'form': form, 'previous_post': previous_post}
        return render(request, 'change_previous_post.html', context)
    return redirect('login')
  
  
def delete_previous_post(request, previous_post_id):
    if request.session.get('user'):
        previous_post = PreviousPost.objects.get(id=previous_post_id)
        if request.method == 'POST':
            previous_post.delete()
            return redirect('previous_post',employee_id=previous_post.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'previous_post': previous_post}
        return render(request, 'delete_previous_post.html', context)
    return redirect('login')


from django.http import HttpResponse
from reportlab.pdfgen import canvas


def download_previous_post(request, previous_post_id):
    # Retrieve the PreviousPost object based on the previouspost_id
    previous_post = PreviousPost.objects.get(id=previous_post_id)

    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="previous_post.pdf"'

    # Create the PDF content
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)

    # Write the heading with employee name
    employee_name = previous_post.employee_id.name
    p.drawString(50, 750, f"Previous Post Information for {employee_name}")

    p.setFont("Helvetica", 12)

    # Write the PreviousPost information to the PDF
    p.drawString(50, 720, f"Denomination: {previous_post.denomination}")
    p.drawString(50, 700, f"Enterprise: {previous_post.enterprise}")
    p.drawString(50, 680, f"Period: {previous_post.period}")
    p.drawString(50, 660, f"Nuisance Factors: {previous_post.nuisance_factors}")

    p.showPage()
    p.save()

    return response