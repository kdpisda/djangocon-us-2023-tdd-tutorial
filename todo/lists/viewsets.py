from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from todo.lists.models import List
from todo.lists.permissions import ListPermission
from todo.lists.serializers import ListSerializer, RetrieveListSerializer

from utils.mixins.viewsets.action_serializer_mapping import (  # isort:skip
    ViewSetActionSerializerMixin,  # isort:skip
)


class ListViewSet(viewsets.ModelViewSet, ViewSetActionSerializerMixin):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    serializer_action_classes = {
        "list": ListSerializer,
        "retrieve": RetrieveListSerializer,
    }
    permission_classes = [IsAuthenticated, ListPermission]

    @extend_schema(responses={200: ListSerializer(many=True)})
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(responses={200: RetrieveListSerializer()})
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
