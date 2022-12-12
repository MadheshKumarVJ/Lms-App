from django.test import TestCase
from django.urls import reverse
from tests.courses.test_model_mixin import Modelmixin


class TestListView(Modelmixin, TestCase):
    def test_course_list_view_redirects_to_login_page(self):
        response = self.client.get((reverse("course:manage_course_list")))
        self.assertRedirects(response, "/accounts/login/?next=/course/mine/")

    def test_course_list_template_used(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse("course:manage_course_list"))
        self.assertTemplateUsed(response, "courses/manage/course/list.html")

    def test_course_create_template_used(self):
        self.client.login(**self.credentials)
        response = self.client.get(reverse("course:create"))
        self.assertTemplateUsed(response, "courses/manage/course/form.html")

    def test_course_edit_template_used(self):
        self.client.login(**self.credentials)
        response = self.client.get(
            reverse("course:edit", args=[self.course1.pk])
        )
        self.assertTemplateUsed(response, "courses/manage/course/form.html")

    def test_course_delete_template_used(self):
        self.client.login(**self.credentials)
        response = self.client.get(
            reverse("course:delete", args=[self.course1.pk])
        )
        self.assertTemplateUsed(response, "courses/manage/course/delete.html")

    def test_module_edit_template_used(self):
        self.add_permission_to_user(permission="Can change module")
        self.client.login(username="maddy", password="123")
        response = self.client.get(
            reverse("course:course_module_update", args=[self.course1.pk])
        )
        self.assertTemplateUsed(response, "courses/manage/module/formset.html")
