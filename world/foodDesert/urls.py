from django.conf.urls import url
from . import views
from django.conf.urls import include,url
from .views import HomePageView, leedata_datasets

#app_name = 'foodDesert'

urlpatterns = [
	url(r'^$', HomePageView.as_view(), name = 'home'),
	url(r'^lee_data/$', leedata_datasets, name = 'leedata')
	#url(r'^foodDesert/(?P<pk>[0-9]+)$',
	#	views.foodDesertsDetailView.as_view(), name = 'foodDesert-detail'),
]

