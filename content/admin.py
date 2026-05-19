from django.contrib import admin
from .models import (
    Hero, TypedRole, AboutSection, AboutParagraph, Stat,
    Experience, ExperienceTag, ContactInfo
)

class TypedRoleInline(admin.TabularInline):
    model = TypedRole
    extra = 1

class AboutParagraphInline(admin.TabularInline):
    model = AboutParagraph
    extra = 1

class StatInline(admin.TabularInline):
    model = Stat
    extra = 1

class ExperienceTagInline(admin.TabularInline):
    model = ExperienceTag
    extra = 1

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    inlines = [TypedRoleInline]

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [AboutParagraphInline, StatInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceTagInline]
    list_display = ('role', 'organization', 'period', 'order')

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'order')