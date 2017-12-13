from django.contrib import admin

from .models import Creditor, Credit


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    list_display = ('created', 'updated', 'rotation_start', 'rotation_end',
                    'name', 'credit_type', 'score_min', 'score_max', 'creditor')
    search_fields = ('name', 'credit_type', 'creditor')
    date_hierarchy = 'created'
    list_filter = ('created', 'updated')


admin.site.register(Creditor)
