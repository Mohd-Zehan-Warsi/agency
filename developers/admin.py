from django.contrib import admin
from .models import (
    Developer,
    DeveloperSkill,
    DeveloperProject,
    DeveloperExperience,
    DeveloperEducation,
)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "designation",
        "email",
        "location",
        "cv",
    )

    search_fields = (
        "name",
        "designation",
        "email",
        "bio",
    )

    ordering = (
        "name",
    )

    fieldsets = (
        (
            "Developer Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "designation",
                    "bio",
                    "photo",
                    "cv",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "location",
                )
            },
        ),
        (
            "Social Links",
            {
                "fields": (
                    "github",
                    "linkedin",
                    "instagram",
                    "website",
                )
            },
        ),
    )


@admin.register(DeveloperSkill)
class DeveloperSkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "developer",
    )

    search_fields = (
        "name",
        "developer__name",
    )


@admin.register(DeveloperProject)
class DeveloperProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "developer",
    )

    search_fields = (
        "title",
        "developer__name",
        "technologies",
    )


@admin.register(DeveloperExperience)
class DeveloperExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "company",
        "developer",
        "start_date",
    )

    search_fields = (
        "position",
        "company",
        "developer__name",
    )


@admin.register(DeveloperEducation)
class DeveloperEducationAdmin(admin.ModelAdmin):

    list_display = (
        "degree",
        "institute",
        "developer",
        "start_year",
    )

    search_fields = (
        "degree",
        "institute",
        "developer__name",
    )