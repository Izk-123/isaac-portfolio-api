from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'emoji', 'order', 'created_at')
    list_filter = ('tags',)
    search_fields = ('title', 'description')
    ordering = ('order',)
    prepopulated_fields = {'gradient': ('title',)}  # optional, if you want to auto‑fill