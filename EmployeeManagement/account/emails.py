from django.core.mail import send_mail

def send_feedback_email(subject,message,from_email,to_email):
    send_mail(subject,message,from_email,to_email,fail_silently=True)