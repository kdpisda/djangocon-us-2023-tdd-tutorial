from rest_framework.permissions import BasePermission


class ItemPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_superuser and not request.user.is_staff:
            return obj.list.user == request.user
        return True
