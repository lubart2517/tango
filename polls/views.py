from django.shortcuts import render

def polls(request):
	response = render(request,'polls/index.html')
	return response

# Create your views here.
