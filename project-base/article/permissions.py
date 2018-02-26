from rest_framework import permissions


class UpdatePermission(permissions.BasePermission):
    """own status update."""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        
        return False 