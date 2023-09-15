from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Пермишен (разрешение) для проверки, является ли текущий пользователь владельцем объекта.
    """
    def has_object_permission(self, request, view, obj):
        """
        Метод для проверки, имеет ли текущий пользователь доступ к объекту.
        Args:
            request: Запрос, выполняемый пользователем.
            view: Представление, в котором проверяется доступ.
            obj: Объект, к которому проверяется доступ.
        Returns:
            bool: True, если пользователь является владельцем объекта, иначе False.
        """
        return request.user == obj.owner


class IsStaff(BasePermission):
    """
    Пермишен (разрешение) для проверки, является ли текущий пользователь сотрудником (staff).
    """
    def has_permission(self, request, view):
        """
        Метод для проверки, имеет ли текущий пользователь статус сотрудника.
        Args:
            request: Запрос, выполняемый пользователем.
            view: Представление, в котором проверяется доступ.
        Returns:
            bool: True, если пользователь является сотрудником, иначе False.
        """
        return request.user.is_staff


class IsUser(BasePermission):
    """
    Пермишен (разрешение) для проверки, является ли текущий пользователь владельцем объекта, связанного с представлением.
    """
    def has_permission(self, request, view):
        """
        Метод для проверки, имеет ли текущий пользователь доступ к объекту представления.
        Args:
            request: Запрос, выполняемый пользователем.
            view: Представление, в котором проверяется доступ.
        Returns:
            bool: True, если пользователь имеет доступ к объекту представления, иначе False.
        """
        return request.user == view.get_object()
