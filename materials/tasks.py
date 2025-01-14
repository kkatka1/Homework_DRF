from datetime import timedelta

from dateutil.utils import today
from django.core.mail import send_mail
from django.utils import timezone
from config import settings
from celery import shared_task
from users.models import User


@shared_task
def subscription_message(course, email):
    send_mail(
        subject="Сообщение о подписке",
        message=f"Материалы курса {course} обновились",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

@shared_task
def block_user():
    now = timezone.now()
    users = User.objects.filter(last_login__lte=now - timedelta(days=30), is_active=True)
    for user in users:
        user.is_active = False
        user.save()




