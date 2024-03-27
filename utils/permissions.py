from rest_framework.permissions import BasePermission


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return False


class IsUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'user':
            return True
        return False
