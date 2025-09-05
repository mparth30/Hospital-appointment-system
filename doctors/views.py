from django.shortcuts import render
from .models import DoctorProfile

def list_doctors(request):
    qs = DoctorProfile.objects.filter(available=True)
    return render(request, 'doctors/list.html', {'doctors': qs})
