from send_mail.celery import app
from django.core.mail import send_mail
from .service import send
from .models import Contact


@app.task
def my_task(a, b):
    c = a + b
    return c


@app.task
def my_task_as(d, e):
    c = d + e
    return c


@app.task(bind=True, default_retry_delay=5 * 10)
def my_task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)


@app.task
def send_spam_email(user_email):
    """Отправляет 1 сообщение при вводе его в форму """
    send(user_email)


@app.task
def send_beat_email():
    """
    Спам на почту через определённый интервал
    """
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписаны на рассылку',
            'Вы подписаны на рассылку',
            'testm2462@gmail.com',
            [contact.email],
            fail_silently=False,
        )
