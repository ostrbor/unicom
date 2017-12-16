from rest_framework import permissions
from unicom.settings import ADMIN_GROUP, PARTNER_GROUP


class AccessToPartnerApi(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name=ADMIN_GROUP).filter(name=PARTNER_GROUP).exists()
