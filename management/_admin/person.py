from django.contrib import admin

from management.models import Family, Person, ResponsibleFamily, Son, VCard


class VcardInline(admin.StackedInline):
    model = VCard
    extra = 1


class ResponsibleFamilyInline(admin.StackedInline):
    model = ResponsibleFamily
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('type', 'is_alive', 'first_name', 'last_name', 'work')
        }),
    )


class FamilyInline(admin.StackedInline):
    model = Family
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('type', 'first_name', 'last_name', 'date_of_birth')
        }),
    )


class SonInline(admin.StackedInline):
    model = Son
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [VcardInline, ResponsibleFamilyInline, FamilyInline, SonInline]
    search_fields = ('first_name', 'last_name', 'religion', 'address')
    list_filter = (
        'is_working',
        'is_healthy',
        'civil_status',
        'education_stage')
    list_display = (
        'first_name',
        'last_name',
        'is_working',
        'is_healthy',
        'is_medicated')
    fieldsets = (
        ('Datos personales', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'dni', 'address', 'civil_status', 'dwelling',)
        }),
        ('Trabajo', {
            'fields': ('is_working', 'work_place')
        }),
        ('Ingreso', {
            'fields': ('income',)
        }),
        ('Salud', {
            'fields': ('is_healthy', 'which_issue')
        }),
        ('Educación', {
            'fields': ('education_stage', 'dropout_reason')
        }),
        ('Religiosidad', {
            'fields': ('religion', 'is_baptized', 'is_communion', 'is_confirmation')
        }),
        ('Observaciones', {
            'fields': ('note',)
        }),
    )
