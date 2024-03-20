from django.shortcuts import render,redirect
from App.models import  Prescription, MedicalRecord, Drugs
from App.models.forms import PrescriptionForm


def display_prescription(request, medical_record_id):
    if request.session.get('user'):
    
        prescriptions = Prescription.objects.filter(medical_record=medical_record_id)
        context = {'prescriptions': prescriptions, 'record': medical_record_id}
        return render(request, 'prescription.html', context)
    return redirect('login')



def add_prescription(request, medical_record_id):
    if request.session.get('user'):
        drugs = Drugs.objects.all()
        if request.method == 'POST':
            form = PrescriptionForm(request.POST)
            if form.is_valid():
                form.save()
                drug = Drugs.objects.get(name = request.POST['drug_name'])
                drug.dosage_issued = drug.dosage_issued + int(request.POST['dosage'])
                drug.quantity= drug.quantity - int(request.POST['dosage'])
                drug.save()
                return redirect('prescription', medical_record_id=medical_record_id)
        else:
            form = PrescriptionForm()
        context = {'record':medical_record_id,'drugs': drugs }
        return render(request, 'add_prescription.html', context)
    return redirect('login')



def change_prescription(request, prescription_id):
    if request.session.get('user'):
        try:
            prescription = Prescription.objects.get(id=prescription_id)
        except Prescription.DoesNotExist:
            return redirect('prescription', medical_record_id=prescription.medical_record_id)

        if request.method == 'POST':
            form = PrescriptionForm(request.POST, instance=prescription)
            if form.is_valid():
                form.save()
                return redirect('prescription', medical_record_id=prescription.medical_record_id)
        else:
            form = PrescriptionForm(instance=prescription)

        context = {'form': form, 'prescription': prescription}
        return render(request, 'change_prescription.html', context)
    return redirect('login')


def delete_prescription(request, prescription_id):
    if request.session.get('user'):
        try:
            prescription = Prescription.objects.get(id=prescription_id)
            medical_record_id = prescription.medical_record_id  # Store the medical record ID before deleting the prescription
            if request.method == 'POST':
                prescription.delete()
                return redirect('prescription', medical_record_id=medical_record_id)
        except Prescription.DoesNotExist:
            return redirect('prescription', medical_record_id=prescription.medical_record_id)
        
        context = {'prescription': prescription}
        return render(request, 'delete_prescription.html', context)
    return redirect('login')