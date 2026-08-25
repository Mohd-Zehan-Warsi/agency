from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=100)

    designation = models.CharField(max_length=150)

    technologies = models.ManyToManyField(
        "projects.Technology",
        blank=True,
        related_name="developers"
    )

    experience = models.CharField(
        max_length=100,
        blank=True
    )

    photo = models.ImageField(
        upload_to="developers/",
        blank=True,
        null=True
    )

    bio = models.TextField(blank=True)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio_url = models.URLField(blank=True)

    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name