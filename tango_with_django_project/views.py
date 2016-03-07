from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
def home(request):
	return render(request, 'home.html')
def send_mail_to(email_subject, email_message):
	send_mail('Your Email subject', 'Your Email message.', 'lubomirvihvatniuk@gmail.com', ['0972985743s@gmail.com'], fail_silently=False)
# Create your views here.
