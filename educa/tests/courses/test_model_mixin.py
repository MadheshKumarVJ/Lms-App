from django.test import TestCase
from courses.models import Subject, Course, Module
from tests.factories import UserFactory


class Modelmixin(TestCase):
    def setUp(self):
        self.credentials = {"username": "maddy", "password": "123"}
        self.user = self.create_user()
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

    def create_user(self):
        return UserFactory(**self.credentials)

    def create_course(self, count, owner=None):
        if owner is None:
            owner = self.user
        for _ in range(count):
            Course.objects.create(
                owner=owner,
                subject=self.subject1,
                title="course1",
                slug="course1",
            )
        return Course.objects.all()
