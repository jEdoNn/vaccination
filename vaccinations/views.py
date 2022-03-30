from django.shortcuts import render, get_object_or_404
from .models import Vaccination
from .models import Manufacturer

def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    return render(request, 'vaccinations/vaccination_list.html', {'vaccinations' : vaccinations})

def vaccination_detail(request, str):
    manufacturer = Manufacturer.objects.all()
    return render(request, 'vaccinations/vaccination_detail.html', {'manufacturer' : manufacturer})