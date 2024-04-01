

from django.shortcuts import render, redirect

def index(request):
    if request.session.get('user'):
        return redirect('display_patient', employee_id = 'all')
    return render(request,'index.html')