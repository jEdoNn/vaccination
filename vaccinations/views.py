from django.shortcuts import render
from .models import Vaccination
from .models import Manufacturer

def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    return render(request, 'vaccinations/vaccination_list.html', {'vaccinations' : vaccinations})

def vaccination_detail(request, str):
    manufacturer = Manufacturer.objects.filter(location=str)
    return render(request, 'vaccinations/vaccination_detail.html', {'manufacturer' : manufacturer})