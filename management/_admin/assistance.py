from django.contrib import admin

from management.models import Activity, Assistance


@admin.register(Assistance)
class AssistanceAdmin(admin.ModelAdmin):
    search_fields = ('activity__title',)
    list_display = ('activity', 'date',)
    list_filter = ('date',)

    def get_queryset(self, request):
        qs = super(AssistanceAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(activity__teacher=request.user)
        return qs

    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['activity'].queryset = request.user.activities.all()
        return super(AssistanceAdmin, self).render_change_form(
            request, context, *args, **kwargs)
