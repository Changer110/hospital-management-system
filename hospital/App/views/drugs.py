

from .import_all import *



def display_drug(request):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        drug_name = request.session.get('drug_name')
        if drug_name:
            drugs = Drugs.objects.filter(name = drug_name)
            request.session['drug_name'] = None
        elif request.method == 'POST':
            request.session['drug_name'] = request.POST.get('drug_name')            
            return redirect('display_drug')
        context = {'drugs' : drugs}
        return render(request, 'drugs.html', context)
    return redirect('login')



def add_drug(request, drug_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = DrugForm(request.POST)
            if form.is_valid():
                drug = form.save()
                request.session['drug_name'] = drug.name
                return redirect('display_drug')
            return redirect('add_drug')
        context = {
            'action' : 'Add',
            'value' : drug_id,
            'sbt' : 'add_drug'
        }
        return render(request, 'drug_form.html', context)
    return redirect('login')



def update_drug(request, drug_id):
    if request.session.get('user'):
        drug = Drugs.objects.get(id = drug_id)
        if request.method == 'POST':
            form = DrugForm(request.POST, instance = drug)
            if form.is_valid():
                form.save()
                request.session['drug_name'] = drug.name
                return redirect('display_drug')
            return redirect('update_drug', drug_id = drug_id)
        context = {
            'drug' : drug,
            'action' : 'Add',
            'value' : drug_id,
            'sbt' : 'update_drug',
        }
        return render(request, 'drug_form.html', context)
    return redirect('login')




def delete_drug(request, drug_id):
    if request.session.get('user'):
        drug = Drugs.objects.get(id = drug_id)
        drug.delete()
        # return JsonResponse({'message': 'Drug deleted successfully'})
    return redirect('login')

