from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from app.models import item

def index(request):
	return HttpResponse("Hello, world.")
def view(request, linkid):
	url = item.objects.get(linkid=linkid)
	response = str(url.link)
	return HttpResponsePermanentRedirect(response)

