from celery import shared_task
from celery.decorators import task

from django.core.mail import send_mail
from celery.utils.log import get_task_logger
logger=get_task_logger(__name__)
# This is the decorator which a celery worker uses
@task(name="send email")
def send_feedback_email(subject,message,from_email,to_email):
	logger.info("Sent email")
	print("heloo celery")
	send_mail(subject,message,from_email,to_email,fail_silently=True)
	return "send email sucessfully."
    