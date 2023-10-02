from datetime import datetime, timedelta, timezone
from celery import shared_task
from users.models import User


@shared_task
def check_inactive_users():
    """
    Асинхронная задача для проверки неактивных пользователей и отключения их активных статусов, если они не входили
    в систему более 30 дней.
    """

    # Получение всех пользователей, исключая тех, у которых last_login равен None.
    users = User.objects.all().exclude(last_login__isnull=True)

    for user in users:
        # Проверяется, прошло ли более 30 дней с момента последнего входа пользователя в систему.
        if datetime.now(timezone.utc) - user.last_login > timedelta(days=30):
            # Устанавливается флаг is_active пользователя в False, что означает неактивный статус.
            user.is_active = False

            user.save()
