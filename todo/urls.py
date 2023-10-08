from django.urls import include, path
from rest_framework.routers import SimpleRouter

from todo.items.viewsets import ItemViewSet
from todo.lists.viewsets import ListViewSet

router = SimpleRouter()

router.register(r"items", ItemViewSet, basename="items")
router.register(r"lists", ListViewSet, basename="lists")

urlpatterns = [
    path("", include(router.urls)),
]
