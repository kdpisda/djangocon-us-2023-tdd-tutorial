from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from iam.user.tests.factories.users import UserFactory
from todo.lists.tests.factories.lists import ListFactory


class TestList(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        self.list = ListFactory(user=self.user)

    def test_get_list(self):
        response = self.client.get(reverse("lists-list"))
        assert response.status_code == status.HTTP_200_OK

        lists = response.json()
        assert len(lists) == 1

    def test_create_list(self):
        response = self.client.post(
            reverse("lists-list"),
            data={
                "name": "Test List",
            },
            type="json",
        )

        assert response.status_code == status.HTTP_201_CREATED
