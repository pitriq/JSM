from django.contrib import admin

from management.models import Dwelling


@admin.register(Dwelling)
class DwellingAdmin(admin.ModelAdmin):
    pass
