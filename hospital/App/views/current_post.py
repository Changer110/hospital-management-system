


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
            return redirect('current_post', employee_id = employee_id)
    context = {'patient' : Patient.objects.get(employee_id = employee_id)}
    return render(request, 'add_current_post.html', context)



def update_current_post(request, employee_id):
    
    return 0



def delete_current_post(request, employee_id):
    
    return 0