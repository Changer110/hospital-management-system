



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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
            page = 'patient'
        return redirect(page, employee_id = 'all')
    return render(request, 'login.html')


# def user_page(request):
#     page = 'login'
#     if request.session.get('user'):
#         return render
#     return redirect([page])