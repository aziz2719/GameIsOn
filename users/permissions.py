from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrCreateUser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff

class UserPermissionOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj == request.user