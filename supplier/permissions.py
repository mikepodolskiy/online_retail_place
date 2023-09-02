from rest_framework import permissions


class IsActivePermission(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        """
        provides permission to api only for active users
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_active
