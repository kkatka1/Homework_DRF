from rest_framework import permissions



class IsModer(permissions.BasePermission):
    """Проверка, что пользователь состоит в группе модераторов"""
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderator').exists()



class IsOwner(permissions.BasePermission):
    """Проверка, что пользователь является владельцем объекта"""
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False