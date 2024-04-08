

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
            'action' : 'update',
            'value' : drug_id,
            'sbt' : 'update_drug',
        }
        return render(request, 'drug_form.html', context)
    return redirect('login')




def delete_drug(request, drug_id):
    if request.session.get('user'):
        drug = Drugs.objects.get(id = drug_id)
        if request.method == 'POST':
            drug.delete()
            return redirect('display_drug')
        context = {
                'drug': drug
            }
        return render(request, 'delete_drug.html', context)
    return redirect('login')



from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_drugs(request):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=drugs_list.pdf'
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        p.drawString(100, 700, "Drugs List")
        p.drawString(100, 675, "------------------------------------")
        y = 650
        for drug in drugs:
            p.drawString(100, y, f"Name: {drug.name}")
            p.drawString(100, y - 25, f"Type: {drug.get_drug_type_display()}")
            p.drawString(100, y - 50, f"Quantity: {drug.quantity}")
            p.drawString(100, y - 75, f"Expiry Date: {drug.expiry_date.strftime('%Y-%m-%d')}")
            p.drawString(100, y - 100, f"Dosage Issued: {drug.dosage_issued}")
            p.drawString(100, y - 125, f"Price: {drug.price}")
            p.drawString(100, y - 150, f"Price Per Drug: {drug.price_per_drug}")
            p.drawString(100, y - 175, f"Imported From: {drug.imported_from}")
            p.drawString(100, y - 200, "------------------------------------")
            y -= 225
        p.save()
        return response
    return redirect('login')