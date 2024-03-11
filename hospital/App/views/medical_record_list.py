from django.shortcuts import render
from App.models import MedicalRecord

def medical_record_list(request):
    records = MedicalRecord.objects.all()
    context = {'records': records}
    return render(request, 'medical_record_list.html', context)