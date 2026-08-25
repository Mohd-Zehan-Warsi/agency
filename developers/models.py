from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    designation = models.CharField(max_length=150)
    bio = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="developers/",
        blank=True,
        null=True
    )

    cv = models.FileField(
        upload_to="developers/cv/",
        blank=True,
        null=True
    )

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)

    location = models.CharField(max_length=150, blank=True)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class DeveloperSkill(models.Model):
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.developer.name} - {self.name}"


class DeveloperProject(models.Model):
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="projects"
    )

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="developers/projects/",
        blank=True,
        null=True
    )

    project_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)

    technologies = models.CharField(
        max_length=300,
        blank=True,
        help_text="Example: Django, React, PostgreSQL"
    )

    def __str__(self):
        return f"{self.developer.name} - {self.title}"


class DeveloperExperience(models.Model):
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    company = models.CharField(max_length=150)
    position = models.CharField(max_length=150)

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.developer.name} - {self.position}"


class DeveloperEducation(models.Model):
    developer = models.ForeignKey(
        Developer,
        on_delete=models.CASCADE,
        related_name="education"
    )

    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=150)
    field = models.CharField(max_length=150, blank=True)

    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.developer.name} - {self.degree}"