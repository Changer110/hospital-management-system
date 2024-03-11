# import necessary modules
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from App.models import Drugs

def delete_drug(request, drug_id):
    # Retrieve the drug object based on the provided drug_id
    drug = get_object_or_404(Drugs, id=drug_id)

    # Perform the delete operation
    drug.delete()

    # Return a JSON response indicating success
    return JsonResponse({'message': 'Drug deleted successfully'})