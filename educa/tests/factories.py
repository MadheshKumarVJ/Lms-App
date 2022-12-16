import factory
from factory import Faker
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


def add_permissions_to_user(obj, permissions):
    for permission in permissions:
        obj.user_permissions.add(Permission.objects.get(codename=permission))


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "user"

    @factory.post_generation
    def password(obj, create, extracted, **kwargs):
        if extracted:
            obj.set_password(extracted)
        else:
            obj.set_password("password")

    @factory.post_generation
    def username(obj, create, extracted, **kwargs):
        if extracted:
            obj.username = extracted

    @factory.post_generation
    def add_permissions(obj, create, extracted, **kwargs):
        add_permissions_to_user(
            obj,
            permissions=[
                "change_course",
                "view_course",
                "delete_course",
                "add_course",
            ],
        )
