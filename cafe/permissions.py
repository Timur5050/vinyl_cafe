from rest_framework import permissions


class IsAdminOrAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            (request.user and request.user.is_authenticated)
            and request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff
        )
