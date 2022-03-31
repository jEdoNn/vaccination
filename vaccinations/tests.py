from django.test import TestCase
from .models import Vaccination

# Create your tests here.
class VaccinationModelTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up test data in database
        Vaccination.objects.create(country = 'Afghanistan',
                iso_code = 'AFG',
                date = '2021/3/2',
                daily_vaccinations = '2008',
                vaccines = 'Oxford/AstraZeneca, Pfizer/BioNTech, Sinopharm/Beijing',
                source_name = 'World Health Organization',
                )
        Vaccination.objects.create(country = 'Antigua and Barbuda',
                iso_code = 'ATG',
                date = '2021/8/5',
                daily_vaccinations = '114',
                vaccines = 'Oxford/AstraZeneca, Pfizer/BioNTech, Sputnik V',
                source_name = 'Ministry of Health',
                )
        
    def test_vaccinations(self):
        vaccination = Vaccination.objects.get(id=1)
        self.assertEqual(vaccination.iso_code, 'AFG')
        vaccinations = Vaccination.objects.all()
        self.assertEqual(vaccinations.count(), 2)