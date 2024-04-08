



from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from .import_all import *




def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'registerform': form}) 


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
            return redirect('display_patient', employee_id = 'all')
        return redirect(page)
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return render(request,'index.html')