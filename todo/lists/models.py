from django.contrib.auth import get_user_model
from django.db import models

from utils.mixins.models.timestamped_model import TimeStampedModel

User = get_user_model()


class Status(models.TextChoices):
    PENDING = "PENDING", "Pending"
    DONE = "DONE", "Done"
    ARCHIVED = "ARCHIVED", "Archived"


class List(TimeStampedModel):
    name = models.CharField(max_length=255, help_text="Name of the list")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, help_text="User who owns the list"
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        help_text="Status of the list",
    )

    def __str__(self):
        return self.name
