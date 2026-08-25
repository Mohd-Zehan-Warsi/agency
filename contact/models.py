from django.db import models
from django.db import models


class ContactMessage(models.Model):

    STATUS_CHOICES = (
        ("new", "New"),
        ("read", "Read"),
        ("replied", "Replied"),
    )

    name = models.CharField(max_length=120)

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    subject = models.CharField(
        max_length=200,
        blank=True
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"
# Create your models here.
