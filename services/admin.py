from django.contrib import admin
from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "short_description",
        "is_active",
        "order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    filter_horizontal = (
        "technologies",
    )

    ordering = (
        "order",
        "id",
    )
# Register your models here.
