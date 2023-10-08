from rest_framework import serializers

from todo.items.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "content",
            "status",
            "created_at",
            "updated_at",
            "deadline",
        )
