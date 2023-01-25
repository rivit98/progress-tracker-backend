from rest_framework.permissions import BasePermission


class HasSpecialProgressViewAccess(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="special_progress_view").exists()
