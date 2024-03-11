from django.shortcuts import render,redirect
from App.models import Enterprise


def enterprise_list(request):
    enterprises = Enterprise.objects.all()
    return render(request, 'enterprise_list.html', {'enterprises': enterprises})



from App.models.forms import EnterpriseForm

def add_enterprise(request):
    if request.method == 'POST':
        form = EnterpriseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enterprise_list')
    else:
        form = EnterpriseForm()
    
    return render(request, 'add_enterprise.html', {'form': form})


def delete_enterprise(request, enterprise_id):
    try:
        enterprise = Enterprise.objects.get(id=enterprise_id)
    except Enterprise.DoesNotExist:
        return redirect('enterprise_list')  # Replace 'enterprise_list' with the appropriate URL name for your enterprise list view

    if request.method == 'POST':
        enterprise.delete()
        return redirect('enterprise_list')  # Replace 'enterprise_list' with the appropriate URL name for your enterprise list view
    
    context = {'enterprise': enterprise}
    return render(request, 'delete_enterprise.html', context)