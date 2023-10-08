from django.contrib.auth import get_user_model
from django.test import TestCase  # noqa F401

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
