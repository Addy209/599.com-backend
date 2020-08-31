from rest_framework.permissions import BasePermission

class IsRegistered(BasePermission):
    """
    Allows access only to Registered users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.registered)