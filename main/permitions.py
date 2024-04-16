from rest_framework import permissions
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method  in permissions.SAFE_METHODS:
            return True
        return bool(obj.user == request.user)
