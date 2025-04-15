from rest_framework import permissions
from rest_framework.request import Request


class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request: Request, view) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class ReviewUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
