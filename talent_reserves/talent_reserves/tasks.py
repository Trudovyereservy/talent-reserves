from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings


@shared_task()
def send_feedback_email_task():
    """Sends an email when the feedback form has been submitted."""
    send_mail(
                'New Feedback Received',
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_RECIPIENT],
                fail_silently=False
            )
