import os
from django.contrib.gis.utils import LayerMapping
from .models import leedata

leedata_mapping = {
    'geom': 'MULTIPOINT',
   # 'name': 'CONTACT_NAME'
}

leedata_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/leedata.shp'))

def run(verbose=True):
	lm = LayerMapping(leedata, leedata_shp, leedata_mapping, transform = False, encoding= 'iso-8859-1')
	lm.save(strict=True,verbose=verbose)