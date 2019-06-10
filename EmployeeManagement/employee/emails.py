from django.core.mail import send_mail

def send_feedback_email(name,email,message):
    send_mail(name,message+" \n "+email,email,['recepients email'],fail_silently=False)