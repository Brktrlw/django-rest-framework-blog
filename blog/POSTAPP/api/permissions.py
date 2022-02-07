from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    message = "Bu objenin sahibi Siz Değilsiniz"
    def has_object_permission(self, request, view, obj):
        return (obj.Author == request.user) or request.user.is_superuser
