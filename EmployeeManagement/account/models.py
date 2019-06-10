from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import get_template,render_to_string
from django.db.models import Q
from EmployeeManagement.utils import random_string_generator, unique_key_generator
from django.contrib.auth import get_user_model
User = get_user_model()

#send_mail(subject, message, from_email, recipient_list, html_message)
DEFAULT_ACTIVATION_DAYS = getattr(settings, 'DEFAULT_ACTIVATION_DAYS', 7)

# Create your models here.


                     
                     



