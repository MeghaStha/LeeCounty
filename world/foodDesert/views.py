from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import TemplateView
from .models import foodDesert
from .models import leedata
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.
def lee(request):
    return render(request,'foodDesert/home.html')

class foodDesertDetailView(DetailView):
    template_name = 'foodDesert/home.html'
    model = foodDesert

class HomePageView(TemplateView):
	template_name = 'index.html'

def leedata_datasets(request):
	lee = serialize('geojson', leedata.objects.all())
	return HttpResponse(lee, content_type='json')