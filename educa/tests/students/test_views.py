from django.test import TestCase
from django.urls import reverse
from tests.courses.test_model_mixin import Modelmixin


class TestViews(Modelmixin, TestCase):
    def test_registration_registers_students(self):
        self.client.post(
            reverse("students:student_registration"),
            data={
                "username": "test",
                "password1": "Test@123",
                "password2": "Test@123",
            },
        )
        response = self.client.get(reverse("students:student_registration"))
        self.assertTrue("test" in response.context["user"].username)
