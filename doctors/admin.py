from django.contrib import admin
from .models import DoctorProfile
@admin.register(DoctorProfile)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user','specialization','experience_years','available')
