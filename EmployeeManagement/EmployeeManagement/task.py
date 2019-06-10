from celery.decorators import shared_task
from celery.utils.log import get_task_logger
from account.emails import send_feedback_email

logger=get_task_logger(__name__)

# This is the decorator which a celery worker uses
@shared_task(name="send_feedback_email_task")
def send_feedback_email_task(subject,message,from_email,to_email):
    logger.info("Sent email")
    return send_feedback_email(subject,message,from_email,to_email)