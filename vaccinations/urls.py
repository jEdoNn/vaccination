from django.urls import path
from . import views

urlpatterns = [
        path('', views.vaccination_list, name='vaccination_list'),
        path('validation/<id>', views.vaccination_detail, name= 'vaccination_detail'),
        ]