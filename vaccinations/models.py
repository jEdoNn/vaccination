from django.conf import settings
from django.db import models
from django.utils import timezone

    # Create your models here.

class Vaccination(models.Model):
    country = models.TextField()
    iso_code = models.TextField()
    date = models.TextField()
    daily_vaccinations = models.TextField()
    vaccines = models.TextField()
    source_name = models.TextField()

    def __str__(self):
        return self.country, self.iso_code, self.date, self.daily_vaccinations, self.vaccines, self.source_name

class Manufacturer(models.Model):
    location = models.TextField()
    date = models.TextField()
    vaccine = models.TextField()
    total_vaccinations = models.TextField()

    def __str__(self):
        return self.location, self.date, self.vaccine, self.total_vaccinations
    