from django.urls import path
from . import views

urlpatterns = [
        path('vaccination_list.html', views.vaccination_list, name='vaccination_list'),
        path('manufacturer/<str:str>', views.vaccination_detail, name= 'vaccination_detail'),
        path('', views.index, name='index'),
        path('500.html', views.page_not_found, name='page_not_found'),
        path('404.html', views.page_error, name='page_error'),
        ]