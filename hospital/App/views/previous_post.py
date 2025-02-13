

from .import_all import *


def display_previous_post(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        previous_posts = PreviousPost.objects.filter(employee_id = employee_id)
        post_id = request.session.get('post_id')
        if post_id:
            previous_posts = PreviousPost.objects.filter(id = post_id)
            request.session['post_id'] = None
        context = {
            'previous_posts' : previous_posts, 
            'patient' : patient
        }
        return render(request, 'previous_post.html', context)
    return redirect('login')




def add_previous_post(request, employee_id):
    if request.session.get('user'):
        patient = Patient.objects.get(employee_id = employee_id)
        if request.method == 'POST':
            form = PreviousPostForm(request.POST)
            if form.is_valid():
                post = form.save()
                request.session['post_id'] = post.pk
                return redirect('display_previous_post', employee_id = employee_id)
            return redirect('add_previous_post', employee_id = employee_id)
        context = {
            'action' : 'Add',
            'patient' : patient,
            'value' : employee_id,
            'sbt' : 'add_previous_post',
            }
        return render(request, 'previous_post_form.html', context)
    return redirect('login')
  
  
  
def update_previous_post(request, previous_post_id):
    if request.session.get('user'):
        previous_post = PreviousPost.objects.get(pk = previous_post_id)
        if request.method == 'POST':
            form = PreviousPostForm(request.POST, instance = previous_post)
            if form.is_valid():
                form.save()
                request.session['post_id'] = previous_post.pk
                return redirect('display_previous_post', employee_id = previous_post.employee_id.employee_id)
            return redirect('update_previous_post', previous_post_id = previous_post_id)
        context = {
            'action' : 'Update',
            'value' : previous_post_id,
            'sbt' : 'update_previous_post',
            'previous_post': previous_post,
            'patient' : previous_post.employee_id
        }
        return render(request, 'previous_post_form.html', context)
    return redirect('login')
  
  
def delete_previous_post(request, previous_post_id):
    if request.session.get('user'):
        previous_post = PreviousPost.objects.get(id=previous_post_id)
        if request.method == 'POST':
            previous_post.delete()
            return redirect('display_previous_post',employee_id=previous_post.employee_id.employee_id)  # Replace 'previous_post_list' with the appropriate URL pattern name for the previous post list view

        context = {'previous_post': previous_post}
        return render(request, 'delete_previous_post.html', context)
    return redirect('login')




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
    employee_name = previous_post.employee_id.employee_name
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