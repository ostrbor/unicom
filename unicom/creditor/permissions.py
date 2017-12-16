from django.db.models import Q
from rest_framework import permissions
from unicom.settings import ADMIN_GROUP, CREDITOR_GROUP


class AccessToCreditorApi(permissions.BasePermission):
    def has_permission(self, request, view):
        query = Q(name=ADMIN_GROUP) | Q(name=CREDITOR_GROUP)
        is_valid = request.user.groups.filter(query).exists()
        return is_valid or request.user.is_superuser
