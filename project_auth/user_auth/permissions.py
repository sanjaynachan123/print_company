from rest_framework.permissions import BasePermission
from .helper import check_end_user, check_super_admin, check_end_user_objects

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return check_super_admin(request)

    def has_object_permission(self, request, view, obj):
        return check_super_admin(request)

class IsEndUser(BasePermission):
    def has_permission(self, request, view):
        return check_end_user(request)
    def has_object_permission(self, request, view, obj):
        return  check_end_user_objects(request,obj)