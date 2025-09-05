from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from django.db.models import Count
@login_required
def index(request):
    total = Appointment.objects.count()
    pending = Appointment.objects.filter(status='Pending').count()
    confirmed = Appointment.objects.filter(status='Confirmed').count()
    cancelled = Appointment.objects.filter(status='Cancelled').count()
    by_status = Appointment.objects.values('status').annotate(c=Count('id'))
    return render(request, 'dashboard/index.html', {'total':total,'pending':pending,'confirmed':confirmed,'cancelled':cancelled,'by_status':by_status})
