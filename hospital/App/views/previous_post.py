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