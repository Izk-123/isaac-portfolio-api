from django.contrib import admin
from .models import SkillCategory, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    ordering = ('order',)

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'icon', 'color', 'order')
    ordering = ('order',)
    inlines = [SkillInline]