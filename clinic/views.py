from django.shortcuts import render
from .models import Patient

def index(request):
    patients = Patient.objects.order_by('-last_name')
    context = {'patients': patients}
    return render(request, 'patients/index.html', context)
