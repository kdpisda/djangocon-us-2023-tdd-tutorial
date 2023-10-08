import factory

from iam.user.tests.factories.users import UserFactory
from todo.lists.models import List, Status


class ListFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = List

    name = factory.Faker("name")
    user = factory.SubFactory(UserFactory)
    status = factory.Faker("random_element", elements=[x[0] for x in Status.choices])
