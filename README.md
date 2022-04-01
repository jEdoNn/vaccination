# Team-assignment

This design is a data query of vaccination status.
It has some info queries and info filters that use features available in Django. The current implementation may need more improvements, but can serve as a starting point for querying the system.


### Prerequisites

We can start developing our application to display the data. Create a new project folder called 'vaccination' and then cd into the folder via the terminal and execute these commands:

```
    pyenv local 3.6.9 # this sets the local version of python to 3.6.9
    python3 -m venv .venv # this creates the virtual environment for you
    source .venv/bin/activate # this activates the virtual environment
    pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```

### Installing

We will use Django (https://www.djangoproject.com) as our web framework for the application. We install that with
```
    pip install django
```
And that will install django version 3.1.3 with its associated dependencies. 

Install Heroku for your system

```
curl https://cli-assets.heroku.com/install.sh | sh 
```
Download CLI from Heroku – ‘standalone installation’.
Then use ‘heroku create’ to add heroku to a git repository and you can use this to deploy
git push heroku master.


## Running the tests

We'll start with reading the csv file as that is simple. 
```
    python3 parse_csv.py
```
If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):
```
    python3 manage.py runserver 0.0.0.0:8000 
```

### And coding style tests

Validate software validity, reliability, whether there are problems in the data
```
from django.test import TestCase
from .models import Vaccination

# Create your tests here.
class VaccinationModelTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up test data in database
        Vaccination.objects.create(country = 'Afghanistan',
                iso_code = 'AFG',
                date = '2021/3/2
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
```

## Heroku deploy log

```
-----> Building on the Heroku-20 stack
-----> Using buildpack: heroku/python
-----> Python app detected
-----> Using Python version specified in runtime.txt
 !     Python has released a security update! Please consider upgrading to python-3.7.13
       Learn More: https://devcenter.heroku.com/articles/python-runtimes
-----> No change in requirements detected, installing from cache
-----> Using cached install of python-3.7.10
-----> Installing pip 21.3.1, setuptools 57.5.0 and wheel 0.37.0
-----> Installing SQLite3
-----> Installing requirements with pip
-----> $ python manage.py collectstatic --noinput
       128 static files copied to '/tmp/build_afd33a4d/static'.
-----> Discovering process types
       Procfile declares types -> web
-----> Compressing...
       Done: 78.7M
-----> Launching...
       Released v15
       https://teamwork-vaccination.herokuapp.com/ deployed to Heroku
```

## Authors

* **JiaDong Gong** 
* **Bo Liu** 
* **TongWei Shi** 