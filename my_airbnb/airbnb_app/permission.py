from rest_framework.permissions import BasePermission


class CheckStatusRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'guest':
            return True
        return False


class CreatePropertyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'host':
            return True
        return False