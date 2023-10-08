from django.contrib.auth import get_user_model
from rest_framework import serializers

from iam.user.serializers import UserSerializer
from todo.items.serializers import ItemSerializer
from todo.lists.models import List

User = get_user_model()


class ListSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(), queryset=User.objects.all()
    )

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
