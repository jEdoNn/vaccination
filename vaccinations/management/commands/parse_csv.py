import csv
import os
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError

from vaccinations.models import Vaccination
from vaccinations.models import Manufacturer

#We use the command tools so that we gain access to our models and database connections
#https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ 


class Command(BaseCommand):
    help = 'Load data from csv'

    def handle(self, *args, **options):

        # drop the data from the table so that if we rerun the file, we don't repeat values
        Vaccination.objects.all().delete()
        Manufacturer.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(str(base_dir) + '/vaccinations/test_data/country_vaccinations.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                

                vaccination = Vaccination.objects.create(
                country = row[0],
                iso_code = row[1],
                date = row[2],
                daily_vaccinations = row[7],
                vaccines = row[12],
                source_name = row[13],
                )
                vaccination.save()
        
        with open(str(base_dir) + '/vaccinations/test_data/country_vaccinations_by_manufacturer.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader) # skip the header line
            for row in reader:
                
                manufacturer = Manufacturer.objects.create(
                location = row[0],
                date = row[1],
                vaccine = row[2],
                total_vaccinations =row[3],
                )
                manufacturer.save()
        

        print("data parsed successfully")