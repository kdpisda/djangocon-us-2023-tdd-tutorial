import factory

from todo.items.models import Item
from todo.lists.models import Status
from todo.lists.tests.factories.lists import ListFactory


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    name = factory.Faker("name")
    list = factory.SubFactory(ListFactory)
    content = factory.Faker("sentence")
    status = factory.Faker("random_element", elements=[x[0] for x in Status.Choices])
