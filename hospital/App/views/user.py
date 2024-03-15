



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
            request.session['doctor'] = user.pk
            page = 'patient'
        return redirect(page)
    return render(request, 'login.html')