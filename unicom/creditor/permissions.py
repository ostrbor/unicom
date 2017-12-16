from rest_framework import permissions
from unicom.settings import ADMIN_GROUP, CREDITOR_GROUP


class AccessToCreditorApi(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=ADMIN_GROUP).filter(name=CREDITOR_GROUP).exists()
