from django.db import models
class Technology(models.Model):
    name = models.CharField(max_length=100)

    slug = models.SlugField(
        max_length=120,
        # unique=True,
        blank=True
    )

    icon = models.ImageField(
        upload_to="technologies/",
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )
    short_description = models.CharField(max_length=255, blank=True)
    detailed_description = models.TextField(
    blank=True,
    default=""
)

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)

    slug = models.SlugField(
        max_length=220,
        #unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    description = models.TextField(
    blank=True,
    default=""
)
    # short_description = models.CharField(max_length=255, blank=True)

    # detailed_description = models.TextField(
    #     blank=True,
    #     default=""
    # )

    project_url = models.URLField(blank=True)

    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="projects"
    )

    developers = models.ManyToManyField(
        "team.Developer",
        blank=True,
        related_name="projects"
    )

    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title