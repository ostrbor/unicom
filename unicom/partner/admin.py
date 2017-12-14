from django.contrib import admin

from .models import Client, ApplicationForCreditor


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated','name', 'middle_name', 'surname',
                    'birth_date', 'phone', 'passport', 'credit_score')
    search_fields = ('name', 'middle_name', 'surname', 'phone', 'passport')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')


@admin.register(ApplicationForCreditor)
class ApplicationForCreditorAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'client',
                    'requested_credit', 'status')
    search_fields = ('client', 'status', 'requested_credit')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')
