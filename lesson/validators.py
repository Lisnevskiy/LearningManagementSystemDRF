from rest_framework import serializers


def validate_lesson_links(value):
    """
    Пользовательский валидатор для проверки ссылок на видеоресурсы урока.
    Args:
        value (str): Ссылка, которую необходимо проверить.
    Raises:
        serializers.ValidationError: Если ссылка не является ссылкой на youtube.com.
    """
    if 'https://www.youtube.com' not in value:
        raise serializers.ValidationError('Запрещено прикреплять ссылки на сторонние ресурсы, кроме youtube.com')
