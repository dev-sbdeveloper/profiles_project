from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Handles editing own profile"""

    def has_object_permission(self, request, view, obj):
        """checks if user is updating own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
