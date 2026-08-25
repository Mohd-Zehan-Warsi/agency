from django.db import models


class AgencySettings(models.Model):
    # Basic agency information
    agency_name = models.CharField(max_length=150, default="My Agency")
    logo = models.ImageField(upload_to="agency/", blank=True, null=True)
    tagline = models.CharField(max_length=255, blank=True)
    about = models.TextField(blank=True)

    # Contact
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    website = models.URLField(blank=True)

    # Social links
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    linktree = models.URLField(blank=True)

    # Hero section
    hero_badge = models.CharField(
        max_length=100,
        default="We build digital experiences"
    )
    hero_title = models.CharField(
        max_length=200,
        default="We Design. We Develop."
    )
    hero_highlight = models.CharField(
        max_length=200,
        default="We Grow Your Business."
    )
    hero_description = models.TextField(
        blank=True,
        default="We create modern websites, web applications and digital experiences."
    )
    hero_primary_text = models.CharField(
        max_length=100,
        default="Explore Services →"
    )
    hero_secondary_text = models.CharField(
        max_length=100,
        default="View Projects"
    )
    hero_image = models.ImageField(
        upload_to="agency/hero/",
        blank=True,
        null=True
    )

    # Stats
    commitment = models.CharField(max_length=20, default="100%")

    # Services section
    # services_badge = models.CharField(
    #     max_length=100,
    #     default="What we do"
    # )
    # services_title = models.CharField(
    #     max_length=150,
    #     default="Our Services"
    # )
    # services_description = models.TextField(
    #     blank=True,
    #     default="Digital solutions designed around your business goals."
    # )

    # Projects section
    projects_badge = models.CharField(
        max_length=100,
        default="Our work"
    )
    projects_title = models.CharField(
        max_length=150,
        default="Featured Projects"
    )
    projects_description = models.TextField(
        blank=True,
        default="Selected work from our agency portfolio."
    )

    # Team section
    team_badge = models.CharField(
        max_length=100,
        default="Our experts"
    )
    team_title = models.CharField(
        max_length=150,
        default="Meet Our Developers"
    )
    team_description = models.TextField(
        blank=True,
        default="Our developers build modern digital experiences."
    )

    # Footer
    footer_text = models.CharField(
        max_length=200,
        default="All rights reserved."
    )

    class Meta:
        verbose_name = "Agency Settings"
        verbose_name_plural = "Agency Settings"

    def __str__(self):
        return self.agency_name


# class Service(models.Model):
    # title = models.CharField(max_length=150)
    # description = models.TextField()
    # icon_text = models.CharField(
    #     max_length=20,
    #     default="✦",
    #     blank=True
    # )
    # icon = models.ImageField(
    #     upload_to="services/",
    #     blank=True,
    #     null=True
    # )
    # is_active = models.BooleanField(default=True)
    # order = models.PositiveIntegerField(default=0)

    # class Meta:
    #     ordering = ["order", "id"]

    # def __str__(self):
    #     return self.title