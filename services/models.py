from django.db import models
from projects.models import Technology
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(max_length=150)

    slug = models.SlugField(
        max_length=170,
        unique=True,
        blank=True
    )
    short_description = models.CharField(
    max_length=255,
    blank=True,
    default="")
    description = models.TextField()


    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="services"
    )

    icon = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    icon_text = models.CharField(
        max_length=20,
        blank=True,
        default="✦"
    )

    is_active = models.BooleanField(default=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title