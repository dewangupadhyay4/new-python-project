from rest_framework.permissions import BasePermission

class IsAdminUsername(BasePermission):
    def has_permission(self, request, view):
        return request.user.username=="admin"