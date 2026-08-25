from django.contrib import admin
from .models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "experience",
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
        "designation",
    )

    search_fields = (
        "name",
        "designation",
        "experience",
        "bio",
    )

    filter_horizontal = (
        "technologies",
    )

    list_editable = (
        "is_active",
        "order",
    )

    ordering = (
        "order",
        "name",
    )

    fieldsets = (
        (
            "Developer Information",
            {
                "fields": (
                    "name",
                    "designation",
                    "technologies",
                    "experience",
                    "photo",
                    "bio",
                )
            },
        ),
        (
            "Social Links",
            {
                "fields": (
                    "github",
                    "linkedin",
                    "portfolio_url",
                )
            },
        ),
        (
            "Settings",
            {
                "fields": (
                    "is_active",
                    "order",
                )
            },
        ),
    )