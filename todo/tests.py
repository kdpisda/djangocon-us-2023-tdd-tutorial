from django.contrib.auth import get_user_model
from django.test import TestCase  # noqa F401
from django.urls import reverse
from rest_framework.test import APIClient

from todo.lists.models import List

User = get_user_model()


class FirstToDoListTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser", password="12345")
        List.objects.create(name="testlist", user=user)

    def test_todo_list(self):
        list = List.objects.get(name="testlist")
        self.assertEquals(list.name, "testlist")
        self.assertEquals(list.user.username, "testuser")


class ListTestCase(TestCase):
    def setUp(self):
        # Creating a user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Initializing the APIClient
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # URL for the API endpoint you're testing
        self.url = reverse("lists-list")  # Replace with the actual endpoint URL

    def test_create_todo_list(self):
        # Data for creating a new list
        data = {"name": "Test List", "status": "PENDING"}

        # Making a POST request to the API endpoint
        response = self.client.post(self.url, data, format="json")

        print(response.json())

        # Verifying if the list was created successfully
        self.assertEqual(response.status_code, 201)
        self.assertEqual(List.objects.count(), 1)
        self.assertEqual(List.objects.get().name, "Test List")
