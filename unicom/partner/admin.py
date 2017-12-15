from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Client, ApplicationForCreditor


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'name_link', 'middle_name', 'surname_link',
                    'birth_date', 'phone', 'passport', 'credit_score')
    search_fields = ('name', 'middle_name', 'surname', 'phone', 'passport')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')

    def name_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:partner_client_change", args=(obj.pk,)),
            obj.name
        ))

    def surname_link(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse("admin:partner_client_change", args=(obj.pk,)),
            obj.surname
        ))

    name_link.short_description = 'name'
    surname_link.short_description = 'surname'


@admin.register(ApplicationForCreditor)
class ApplicationForCreditorAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'updated', 'client',
                    'requested_credit', 'status')
    search_fields = ('client', 'status', 'requested_credit')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')
