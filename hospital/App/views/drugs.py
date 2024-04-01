
from App.models import Drugs
from App.models.forms import AddDrugForm
from django.shortcuts import render, redirect



def display_drugs(request):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        context = {'drugs': drugs}
        return render(request, 'drugs.html', context)
    return redirect('login')



def add_drug(request):
    if request.session.get('user'):
        if request.method == 'POST':
            form = AddDrugForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('drugs')
        context = {'types': ['Tablet','Capsule','Liquid','Injection','Cream','Spray']}
        return render(request, 'add_drug.html', context)
    return redirect('login')


def search_drug(request):
    if request.session.get('user'):
        if request.method == 'POST':
            drug_name = request.POST.get('drug_name')
            drugs = Drugs.objects.filter(name=drug_name)
            return render(request, 'drugs.html', {'drugs': drugs})
        return render(request, 'drugs.html', {'drugs': None})
    return redirect('login')


def show_all_drugs(request):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        return render(request, 'drugs.html', {'drugs': drugs})
    return redirect('login')


from django.http import HttpResponse
from reportlab.pdfgen import canvas

def download_drugs(request):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        
        # Create the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=drugs_list.pdf'
        
        # Generate the PDF content using reportlab
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        
        # Write drugs information in PDF
        p.drawString(100, 700, "Drugs List")
        p.drawString(100, 675, "------------------------------------")
        
        y = 650  # Starting y-coordinate for drug details
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


