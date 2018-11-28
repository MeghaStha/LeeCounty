from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .models import foodDesert
from .models import popdata
from .models import foodlo
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.
#def lee(request):
 #   return render(request,'foodDesert/home.html')

#class foodDesertDetailView(DetailView):
 #   template_name = 'foodDesert/home.html'
  #  model = foodDesert

class HomePageView(TemplateView):
	template_name = 'index.html'

def lee_datasets(request):
	lee = serialize('geojson', popdata.objects.all())
	return HttpResponse(lee, content_type='json')

def leefood_datasets(request):
	leefood = serialize('geojson', foodlo.objects.all())
	return HttpResponse(leefood, content_type='json')