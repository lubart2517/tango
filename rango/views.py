from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return HttpResponse("Rango says Hello <br/> <a href='/rango/about'>About</a")
def about(request):
	return HttpResponse("About Rango <br/> <a href='/rango'>Home page</a")
# Create your views here.
