from rest_framework import serializers

from iam.user.serializers import UserSerializer
from todo.items.serializers import ItemSerializer
from todo.lists.models import List


class ListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = List
        fields = ["name", "user", "status", "created_at", "updated_at", "deadline"]


class RetrieveListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ItemSerializer(many=True)

    class Meta:
        model = List
        fields = [
            "name",
            "user",
            "status",
            "created_at",
            "updated_at",
            "items",
            "deadline",
        ]
