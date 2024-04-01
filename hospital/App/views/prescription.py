
from .import_all import *


def display_prescription(request, medical_record_id):
    if request.session.get('user'):
        prescriptions = Prescription.objects.filter(medical_record = medical_record_id)
        context = {'prescriptions': prescriptions, 'record': medical_record_id}
        return render(request, 'prescription.html', context)
    return redirect('login')



def add_prescription(request, medical_record_id):
    if request.session.get('user'):
        if request.method == 'POST':
            form = PrescriptionForm(request.POST)
            if form.is_valid():
                form.save()
                drug = Drugs.objects.get(name = request.POST['drug_name'])
                drug.dosage_issued = drug.dosage_issued + int(request.POST['dosage'])
                drug.quantity = drug.quantity - int(request.POST['dosage'])
                drug.save()
                return redirect('display_prescription', medical_record_id = medical_record_id)
            return redirect('')
        context = {
            'action' : 'Add',
            'sbt' : 'add_prescription',
            'record' : medical_record_id,
            'drugs' : Drugs.objects.all()
            }
        return render(request, 'prescription_form.html', context)
    return redirect('login')



def change_prescription(request, prescription_id):
    if request.session.get('user'):
        prescription = Prescription.objects.get(id = prescription_id)
        if request.method == 'POST':
            form = PrescriptionForm(request.POST, instance=prescription)
            if form.is_valid():
                form.save()
                # drug = Drugs.objects.get(name = request.POST['drug_name'])
                # drug.dosage_issued = drug.dosage_issued + int(request.POST['dosage'])
                # drug.quantity = drug.quantity - int(request.POST['dosage'])
                # drug.save()
                return redirect('prescription', medical_record_id = prescription.medical_record.pk)
            return redirect('change_prescription', prescription_id = prescription_id)
            
        context = {
            'action' : 'Update',
            'record' : prescription_id,
            'sbt' : 'change_prescription',
            'drugs' : Drugs.objects.all(),
            'prescription' : prescription,
            }
        return render(request, 'prescription_form.html', context)
    return redirect('login')


def delete_prescription(request, prescription_id):
    if request.session.get('user'):
        try:
            prescription = Prescription.objects.get(id=prescription_id)
            medical_record_id = prescription.medical_record_id
            if request.method == 'POST':
                prescription.delete()
                return redirect('prescription', medical_record_id=medical_record_id)
        except Prescription.DoesNotExist:
            return redirect('prescription', medical_record_id=prescription.medical_record_id)
        
        context = {'prescription': prescription}
        return render(request, 'delete_prescription.html', context)
    return redirect('login')




def download_prescription(request, prescription_id):
    if request.session.get('user'):
        prescription = Prescription.objects.get(id=prescription_id)
        patient = prescription.medical_record.patient  # Assuming 'patient' is a field in the MedicalRecord model
        
        # Create the PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=prescription_{patient.employee_name}.pdf'
        
        # Generate the PDF content using reportlab
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        
        # Write prescription information in PDF
        p.drawString(100, 700, f"Prescription Information for {patient.employee_name}")
        p.drawString(100, 675, "------------------------------------")
        p.drawString(100, 650, f"Drug Name: {prescription.drug_name}")
        p.drawString(100, 625, f"Dosage: {prescription.dosage}")
        p.drawString(100, 600, "------------------------------------")
        
        p.save()
        
        return response
    
    return redirect('login')