from django.db import models

from todo.lists.models import List, Status
from utils.mixins.models.timestamped_model import TimeStampedModel


class Item(TimeStampedModel):
    name = models.CharField(max_length=255, help_text="Name of the item")
    content = models.TextField(help_text="Content of the item")
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="items",
        help_text="List to which the item belongs",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        help_text="Status of the item",
    )
    deadline = models.DateTimeField(
        null=True, blank=True, help_text="Deadline of the item"
    )

    def __str__(self):
        return self.list.name
