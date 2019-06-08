from django.contrib import admin

from management.models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    pass
