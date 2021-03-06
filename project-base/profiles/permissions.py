from rest_framework import permissions


class UserUpdatePermission(permissions.BasePermission):
    """Allow users to edit their own profiles."""

    def has_object_permission(self, request, view, obj):
        """Return True if own user is requested user. otherwish False."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class FeedUpdatePermission(permissions.BasePermission):
    """Allow user to updating their own status."""

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user.id == request.user.id
