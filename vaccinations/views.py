from django.shortcuts import render, get_object_or_404
from .models import Vaccination

def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    return render(request, 'vaccinations/vaccination_list.html', {'vaccinations' : vaccinations})

def vaccination_detail(request, id):
    vaccination = get_object_or_404(Vaccination, id=string)
    return render(request, 'vaccinations/vaccination_detail.html', {'country' : country})