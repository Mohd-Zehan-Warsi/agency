from django.shortcuts import render, get_object_or_404

from core.models import AgencySettings
from projects.models import Project, Technology
from team.models import Developer
from services.models import Service


def home(request):
    projects = (
        Project.objects
        .all()
        .prefetch_related("technologies")
    )

    developers = (
        Developer.objects
        .filter(is_active=True)
        .order_by("order", "id")
    )

    services = (
        Service.objects
        .filter(is_active=True)
        .order_by("order", "id")
        .prefetch_related("technologies")
    )

    technologies = Technology.objects.all()

    agency = AgencySettings.objects.first()

    context = {
        "agency": agency,
        "projects": projects,
        "developers": developers,
        "services": services,
        "technologies": technologies,
    }
    return render(request, "index.html", context)


def technology_detail(request, slug):
    technology = get_object_or_404(
        Technology,
        slug=slug
    )

    return render(
        request,
        "tech/technology_detail.html",
        {"technology": technology}
    )