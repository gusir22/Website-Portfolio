# portfolio/admin.py
from django.contrib import admin

from .models import (
    Technology,
    FeaturedProject,
    Screenshot,
    QuickProject,
)


class TechnologyAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
    ]

    search_fields = [
        "__str__",
    ]


admin.site.register(Technology, TechnologyAdmin)


class ScreenshotInline(admin.TabularInline):
    """Admin registration for FeaturedProject inline screenshots"""
    model = Screenshot


class FeaturedProjectAdmin(admin.ModelAdmin):
    inlines = [
        ScreenshotInline,
    ]

    list_display = [
        "__str__",
        "date_completed",
    ]

    list_filter = [
        "date_completed",
        "technologies_used",
    ]

    search_fields = [
        "__str__",
        "date_completed",
        "technologies_used",
    ]


admin.site.register(FeaturedProject, FeaturedProjectAdmin)


class QuickProjectAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "date_completed",
    ]

    list_filter = [
        "date_completed",
        "technologies_used",
    ]

    search_fields = [
        "__str__",
        "date_completed",
        "technologies_used",
    ]


admin.site.register(QuickProject, QuickProjectAdmin)
