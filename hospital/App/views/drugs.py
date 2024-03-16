
from App.models import Drugs
from App.models.forms import AddDrugForm
from django.shortcuts import render, redirect



def display_drugs(request):
    drugs = Drugs.objects.all()
    context = {'drugs': drugs}
    return render(request, 'drugs.html', context)



def add_drug(request):
    if request.method == 'POST':
        form = AddDrugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drugs')
    context = {'types': ['Tablet','Capsule','Liquid','Injection','Cream','Spray']}
    return render(request, 'add_drug.html', context)



def search_drug(request):
    if request.method == 'POST':
        drug_name = request.POST.get('drug_name')
        drugs = Drugs.objects.filter(name=drug_name)
        return render(request, 'drugs.html', {'drugs': drugs})
    return render(request, 'drugs.html', {'drugs': None})


def show_all_drugs(request):
    drugs = Drugs.objects.all()
    return render(request, 'drugs.html', {'drugs': drugs})


