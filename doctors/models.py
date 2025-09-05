from django.db import models
from django.conf import settings

class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=200)
    experience_years = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.user.username} - {self.specialization}"
