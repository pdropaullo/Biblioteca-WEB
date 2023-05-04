from django.contrib import admin
from .models import Midias


class AdminMidias(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_year', 'director', 'description', 'created_at']
    search_fields = ['title']
    list_filter = ['release_year']
    list_display_links = ['title']


admin.site.register(Midias, AdminMidias)