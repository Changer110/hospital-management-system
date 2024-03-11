from django.shortcuts import render
from App.models import Drugs

def drugs(request):
    drugs = Drugs.objects.all()
    context = {'drugs': drugs}
    return render(request, 'drugs.html', context)


def search_drug(request):
    if request.method == 'POST':
        drug_name = request.POST.get('drug_name')
        drugs = Drugs.objects.filter(name=drug_name)
        return render(request, 'drugs.html', {'drugs': drugs})
    return render(request, 'drugs.html', {'drugs': None})


def show_all_drugs(request):
    drugs = Drugs.objects.all()
    return render(request, 'drugs.html', {'drugs': drugs})


