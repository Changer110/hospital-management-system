from django.shortcuts import render, redirect
from App.models.forms import AddDrugForm

def add_drug(request):
    if request.method == 'POST':
        form = AddDrugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drugs')
    else:
        form = AddDrugForm()
        
    context = {'form': form}
    return render(request, 'add_drug.html', context)