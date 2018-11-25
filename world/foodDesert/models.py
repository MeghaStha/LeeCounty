from django.db import models
#from _future_ import unicode_literals

# Create your models here.
#from django import models
from django.contrib.gis.db import models as geomodels

class foodDesert(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    geometry = geomodels.PointField(srid=3160)
    #location = models.CharField(max_length = 50, blank = True)
    #objects = geomodels.GeoManager()

    def _unicode(self):
    	return self.name

    class Meta:
        #order of drop-down list items
        ordering = ('name',)

        #plural form in admin view
        verbose_name_plural = 'foodDesert'

class leedata(models.Model):
    geom = geomodels.MultiPointField(srid=3160)

    #def _unicode_(self):
    #	return self.
