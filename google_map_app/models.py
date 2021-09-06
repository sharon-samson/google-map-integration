from django.db import models

# Create your models here.

from django.db import models
from geoposition.fields import GeopositionField

class Zone(models.Model):
    name = models.CharField(max_length = 50 )
    kuerzel = models.CharField(max_length = 3 )
    kn_nr = models.CharField(max_length = 5 )
    beschreibung = models.CharField(max_length = 300 )
    adresse = models.CharField(max_length = 100 )
    position = GeopositionField()
