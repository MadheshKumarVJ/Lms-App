from tests.courses.test_model_mixin import Modelmixin
from django.test import TestCase


class TestModel(Modelmixin, TestCase):
    def test_order_field_generates_order_number_automatically(self):
        modules = self.create_modules(count=5)
        self.assertEqual(modules.first().order, 0)
        self.assertEqual(modules.last().order, 4)

    def test_order_field_accepts_custom_order_number(self):
        module = self.create_modules(count=1, order_number=10)
        self.assertEqual(module.last().order, 10)
