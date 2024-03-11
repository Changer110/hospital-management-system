from django.shortcuts import render
from App.models import Drugs

def drug_list(request):
    drugs = Drugs.objects.all()
    context = {'drugs': drugs}
    return render(request, 'drug_list.html', context)