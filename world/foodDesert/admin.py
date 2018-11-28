from django.contrib import admin
from .models import foodDesert
from .models import foodlo
from .models import popdata
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class foodDesertAdmin(LeafletGeoAdmin):
	list_display = ('name', 'geometry')

class foodloAdmin(LeafletGeoAdmin):
	list_display = ('company_na','naics_desc')
	#pass
	
class popdataAdmin(LeafletGeoAdmin):
	#list_display = ('geom','')
	pass

admin.site.register(foodDesert, foodDesertAdmin)
admin.site.register(foodlo, foodloAdmin)
admin.site.register(popdata, popdataAdmin)
