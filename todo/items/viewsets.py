from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.items.models import Item
from todo.items.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
