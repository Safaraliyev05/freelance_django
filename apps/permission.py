from rest_framework.permissions import BasePermission

from apps.models import User


class IsFreelancer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        return user.role == User.Type.FREELANCER


class IsBOwner(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False

        return user.role == User.Type.BUSINESS_OWNER


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser
