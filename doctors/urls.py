from django.urls import path
from .views import list_doctors
urlpatterns = [path('list/', list_doctors, name='doctors_list')]
