from django.shortcuts import render, get_object_or_404, redirect
from App.models.forms import ChangeDrugForm  # Import the form for changing drug details
from App.models import Drugs  # Import the Drug model

def change_drug(request, drug_id):
    if request.session.get('user'):
        drug = get_object_or_404(Drugs, id=drug_id)  # Retrieve the drug object using the drug_id

        if request.method == 'POST':
            form = ChangeDrugForm(request.POST, instance=drug)
            if form.is_valid():
                form.save()
                return redirect('/drugs', drug_id=drug_id)  # Redirect to the drug detail page
        else:
            form = ChangeDrugForm(instance=drug)

        return render(request, 'change_drug.html', {'form': form, 'drug': drug})
    return redirect('login')