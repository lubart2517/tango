from django.core.mail import send_mail
 
send_mail('Your Email subject', 'Your Email message.', 'lubomirvihvatniuk@gmail.com', ['0972985743s@gmail.com'], fail_silently=False)