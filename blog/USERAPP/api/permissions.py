from rest_framework.permissions import BasePermission

class isauthenticated(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.Author == request.user