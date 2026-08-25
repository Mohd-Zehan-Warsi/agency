from django.shortcuts import get_object_or_404, render
from .models import Developer


def developer_list(request):
    developers = Developer.objects.all()

    return render(
        request,
        "developers/developer_list.html",
        {
            "developers": developers,
        }
    )


def developer_detail(request, slug):
    developer = get_object_or_404(
        Developer.objects.prefetch_related(
            "skills",
            "projects",
            "experiences",
            "education",
        ),
        slug=slug
    )

    return render(
        request,
        "developers/developer_detail.html",
        {
            "developer": developer,
        }
    )