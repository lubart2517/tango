from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	context_dict = {'boldmessage': "I am bold "}
	return render(request, 'rango/index.html', context_dict)
def about(request):
	return HttpResponse("About Rango <br/> <a href='/rango'>Home page</a")
# Create your views here.
