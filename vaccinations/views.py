from django.shortcuts import render
from .models import Vaccination
from .models import Manufacturer

def index(request):
    return render(request,'vaccinations/index.html')

def vaccination_list(request):
    vaccinations = Vaccination.objects.all()
    return render(request, 'vaccinations/vaccination_list.html', {'vaccinations' : vaccinations})

def vaccination_detail(request, str):
    manufacturer = Manufacturer.objects.filter(location=str)
    return render(request, 'vaccinations/vaccination_detail.html', {'manufacturer' : manufacturer})

def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response

def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response