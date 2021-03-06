from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminUserClubCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff


class IsAdminOrCreateClub(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_superuser or request.user.is_staff


class UserPermissionOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user or obj.owner == request.user.is_staff or request.user.is_superuser
