from django.test import TestCase
from courses.models import Subject, Course, Module
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class Modelmixin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="maddy",
            password="123",
        )
        self.subject1 = Subject.objects.create(
            title="sub1",
            slug="sub1",
        )
        self.course1 = Course.objects.create(
            owner=self.user,
            subject=self.subject1,
            title="course1",
            slug="course1",
        )

    def create_modules(self, count, order_number=None):
        for _ in range(count):
            Module.objects.create(
                course=self.course1, title="testmodule", order=order_number
            )
        return Module.objects.all()

    def add_permission_to_user(self, permission):
        return self.user.user_permissions.add(
            Permission.objects.get(name=permission)
        )
