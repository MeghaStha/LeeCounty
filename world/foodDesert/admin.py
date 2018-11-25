from django.contrib import admin
from .models import foodDesert
from .models import leedata
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class foodDesertAdmin(LeafletGeoAdmin):
	list_display = ('name', 'geometry')

class leedataAdmin(LeafletGeoAdmin):
	#list_display = ('geom','')
	pass
	
admin.site.register(foodDesert, foodDesertAdmin)
admin.site.register(leedata, leedataAdmin)
