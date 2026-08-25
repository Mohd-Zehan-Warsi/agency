from django.contrib import admin
from django.contrib import admin
from .models import AgencySettings


@admin.register(AgencySettings)
class AgencySettingsAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Agency Information",
            {
                "fields": (
                    "agency_name",
                    "logo",
                    "tagline",
                    "about",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "address",
                    "website",
                )
            },
        ),
        (
            "Social Links",
            {
                "fields": (
                    "linkedin",
                    "github",
                    "instagram",
                    "facebook",
                    "linktree",
                )
            },
        ),
        (
            "Hero Section",
            {
                "fields": (
                    "hero_badge",
                    "hero_title",
                    "hero_highlight",
                    "hero_description",
                    "hero_primary_text",
                    "hero_secondary_text",
                    "hero_image",
                )
            },
        ),
        (
            "Stats",
            {
                "fields": ("commitment",)
            },
        ),
        (
            "Projects Section",
            {
                "fields": (
                    "projects_badge",
                    "projects_title",
                    "projects_description",
                )
            },
        ),
        (
            "Team Section",
            {
                "fields": (
                    "team_badge",
                    "team_title",
                    "team_description",
                )
            },
        ),
    
     
        (
            "Footer",
            {
                "fields": ("footer_text",)
            },
        ),
    )

    def has_add_permission(self, request):
        # Keep only one settings object.
        return not AgencySettings.objects.exists()


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ("title", "is_active", "order")
#     list_filter = ("is_active",)
#     search_fields = ("title", "description")
#     ordering = ("order", "id")
# Register your models here.
