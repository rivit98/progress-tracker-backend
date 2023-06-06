from rest_framework.permissions import SAFE_METHODS, BasePermission


class HasSpecialProgressViewAccess(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="games_special").exists()


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
