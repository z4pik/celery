from django.core.mail import send_mail


def send(user_email):
    """Отправка сообщенй на почту"""
    send_mail(
        'Вы подпсаны на рассылку',
        'Теперь вам будет приходть много сообщений',
        'testm2462@gmail.com',
        [user_email],
        fail_silently=False,
    )