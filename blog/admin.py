from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published')
    search_fields = ('title', 'author__email')
    list_filter = ('visible', ('date_published', DateFieldListFilter))
