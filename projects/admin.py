# from django.contrib import admin
# from django.contrib import admin
# from .models import Technology, Project


# @admin.register(Technology)
# class TechnologyAdmin(admin.ModelAdmin):
#     list_display = (
#         "name",
#         "category",
#         "is_active",

#         "order",
#     )

#     list_filter = (
#         "category",
#         "is_active",
#     )

#     search_fields = (
#         "name",
#         "category",
#         #"description"
#         "short_description",
#         "detailed_description",
#     )

#     ordering = (
#         "order",
#         "name",
#     )


# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = (
#         "title",
#         "category",
#         "is_featured",
#         "is_active",
#         "order",
#     )

#     list_filter = (
#         "category",
#         "is_featured",
#         "is_active",
#     )

#     search_fields = (
#         "title",
#         "description",
#         "category",
#     )

#     prepopulated_fields = {
#         "slug": ("title",),
#     }

#     filter_horizontal = (
#         "technologies",
#         "developers",
#     )

#     ordering = (
#         "order",
#         "-id",
#     )
# # Register your models here.
#fffffffffffffffffffffffffff
from django.contrib import admin
from .models import Technology, Project


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "category",
        "short_description",
        "detailed_description",
    )

    ordering = (
        "order",
        "name",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "is_featured",
        "is_active",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
        "category",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = (
        "technologies",
        "developers",
    )

    ordering = (
        "order",
        "-id",
    )