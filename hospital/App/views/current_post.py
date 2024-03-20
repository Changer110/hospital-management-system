


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



def update_current_post(request, current_post_id):
    if request.session.get('user'):
        current_post = CurrentPost.objects.get(id=current_post_id)

        if request.method == 'POST':
            form = CurrentPostForm(request.POST, instance=current_post)
            if form.is_valid():
                form.save()
                return redirect('current_post', employee_id=current_post.employee_id.employee_id )
        else:
            form = CurrentPostForm(instance=current_post)

        context = {'form': form, 'current_post': current_post}
        return render(request, 'update_current_post.html', context)
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