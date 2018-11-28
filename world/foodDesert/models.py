from django.db import models
#from _future_ import unicode_literals

# Create your models here.
#from django import models
from django.contrib.gis.db import models as models

class foodDesert(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    geometry = models.PointField(srid=3160)
    #location = models.CharField(max_length = 50, blank = True)
    #objects = geomodels.GeoManager()

    def _unicode(self):
    	return self.name

    class Meta:
        #order of drop-down list items
        ordering = ('name',)

        #plural form in admin view
        verbose_name_plural = 'foodDesert'

class foodlo(models.Model):
    contact_na = models.CharField(max_length=254)
    company_na = models.CharField(max_length=254)
    primary_ad = models.CharField(max_length=254)
    primary_ci = models.CharField(max_length=254)
    census_tra = models.BigIntegerField()
    census_blo = models.BigIntegerField()
    x = models.FloatField()
    latitude = models.BigIntegerField()
    y_1 = models.FloatField()
    y = models.FloatField()
    longitude = models.BigIntegerField()
    naics_code = models.BigIntegerField()
    naics_desc = models.CharField(max_length=254)
    gender = models.CharField(max_length=254)
    title_desc = models.CharField(max_length=254)
    contact_et = models.CharField(max_length=254)
    hq_branch_field = models.CharField(max_length=254)
    year_first = models.BigIntegerField()
    population = models.CharField(max_length=254)
    source = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
    	return self.naics_desc

class popdata(models.Model):
    objectid = models.BigIntegerField()
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    tractce = models.CharField(max_length=6)
    blkgrpce = models.CharField(max_length=1)
    geoid = models.CharField(max_length=12)
    namelsad = models.CharField(max_length=13)
    mtfcc = models.CharField(max_length=5)
    funcstat = models.CharField(max_length=1)
    aland = models.FloatField()
    awater = models.FloatField()
    intptlat = models.CharField(max_length=11)
    intptlon = models.CharField(max_length=12)
    geo_id = models.FloatField()
    id_12 = models.FloatField()
    geo_id2 = models.FloatField()
    geo_displa = models.CharField(max_length=254)
    d001 = models.BigIntegerField()
    area = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    popden = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


    def __unicode__(self):
        return self.popden