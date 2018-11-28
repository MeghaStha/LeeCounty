from django.conf.urls import url
from . import views
#from django.conf.urls import include,url
from .views import HomePageView, lee_datasets, leefood_datasets

#app_name = 'foodDesert'

urlpatterns = [
   url(r'^$', HomePageView.as_view(), name = 'home'),
   url(r'^popden/$', lee_datasets, name = 'leedata'),
   url(r'^foodlo/$', leefood_datasets, name = 'foodlo')
   #url(r'^foodDesert/(?P<pk>[0-9]+)$',
    #   views.foodDesertsDetailView.as_view(), name = 'foodDesert-detail'),
]
