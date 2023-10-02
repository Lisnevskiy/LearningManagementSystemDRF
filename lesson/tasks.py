from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from course.models import Course
from subscription.models import Subscription


@shared_task()
def send_update_email():
    """
    Асинхронная Celery задача для отправки уведомлений об обновлениях курсов.
    Эта задача итерируется по всем курсам в базе данных и проверяет,
    есть ли у подписанных пользователей активные подписки на обновления по этому курсу.
    Если есть, то отправляет им уведомления по электронной почте.
    """
    courses = Course.objects.all()

    # Проверяем, если есть хотя бы один курс
    if courses.exists():
        for course in courses:
            # Получаем все подписки, связанные с этим курсом
            subscriptions = Subscription.objects.filter(course=course.id)
            if subscriptions:
                for subscription in subscriptions:
                    user = subscription.user
                    # Отправляем электронное письмо на адрес пользователя
                    send_mail(
                        subject=f'{course.title} обновлен',
                        message='Добавлен новый урок',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email]
                    )
