import os
from django.contrib.gis.utils import LayerMapping
from .models import foodlo
from .models import popdata

foodlocation_mapping = {
    'contact_na': 'CONTACT_NA',
    'company_na': 'COMPANY_NA',
    'primary_ad': 'PRIMARY_AD',
    'primary_ci': 'PRIMARY_CI',
    'census_tra': 'CENSUS_TRA',
    'census_blo': 'CENSUS_BLO',
    'x': 'X',
    'latitude': 'LATITUDE',
    'y_1': 'Y_1',
    'y': 'Y',
    'longitude': 'LONGITUDE',
    'naics_code': 'NAICS_CODE',
    'naics_desc': 'NAICS_DESC',
    'gender': 'GENDER',
    'title_desc': 'TITLE_DESC',
    'contact_et': 'CONTACT_ET',
    'hq_branch_field': 'HQ_BRANCH_',
    'year_first': 'YEAR_FIRST',
    'population': 'POPULATION',
    'source': 'SOURCE',
    'geom': 'MULTIPOINT',
}


foodlocation_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/leedata26_food.shp'))

def run(verbose=True):
	lm = LayerMapping(foodlo, foodlocation_shp, foodlocation_mapping, transform = False, encoding= 'iso-8859-1')
	lm.save(strict=True,verbose=verbose)


popdata_mapping = {
    'objectid': 'OBJECTID',
    'statefp': 'STATEFP',
    'countyfp': 'COUNTYFP',
    'tractce': 'TRACTCE',
    'blkgrpce': 'BLKGRPCE',
    'geoid': 'GEOID',
    'namelsad': 'NAMELSAD',
    'mtfcc': 'MTFCC',
    'funcstat': 'FUNCSTAT',
    'aland': 'ALAND',
    'awater': 'AWATER',
    'intptlat': 'INTPTLAT',
    'intptlon': 'INTPTLON',
    'geo_id': 'GEO_id',
    'id_12': 'id_12',
    'geo_id2': 'GEO_id2',
    'geo_displa': 'GEO_displa',
    'd001': 'D001',
    'area': 'area',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'popden': 'popden',
    'geom': 'MULTIPOLYGON',
}


leepop_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/lee_pop_project.shp'))

def run(verbose=True):
	lm = LayerMapping(popdata, leepop_shp, popdata_mapping, transform = 4326, encoding= 'iso-8859-1')
	lm.save(strict=True,verbose=verbose)

