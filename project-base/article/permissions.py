from rest_framework import permissions


class ArticleUpdatePermission(permissions.BasePermission):
    """own Article Update and Delete permission."""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        
        return obj.author.id == request.user.id 


class CommentUpdatePermission(permissions.BasePermission):
    """Own Comment Update and Delete permission."""

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.created_by.id == request.user.id