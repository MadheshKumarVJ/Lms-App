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
        self.client.login(**self.credentials)
        response = self.client.get(
            reverse("course:course_module_update", args=[self.course1.pk])
        )
        self.assertTemplateUsed(response, "courses/manage/module/formset.html")

    def test_module_content_list_template_used(self):
        self.create_modules(1)
        self.client.login(username="maddy", password="123")
        response = self.client.get(
            reverse("course:module_content_list", args=[self.course1.pk])
        )
        self.assertTemplateUsed(
            response, "courses/manage/module/content_list.html"
        )

    def test_text_content_get_stored_in_module_contents(self):
        text_content = self.create_text()
        module_content = self.create_module_content(content=text_content)
        self.assertEqual(text_content, module_content.item)

    def test_image_content_get_stored_in_module_contents(self):
        image_content = self.create_image()
        module_content = self.create_module_content(content=image_content)
        self.assertEqual(image_content, module_content.item)

    def test_video_content_get_stored_in_module_contents(self):
        video_content = self.create_video_url()
        module_content = self.create_module_content(content=video_content)
        self.assertEqual(video_content, module_content.item)

    def test_file_content_get_stored_in_module_contents(self):
        file_content = self.create_file()
        module_content = self.create_module_content(content=file_content)
        self.assertEqual(file_content, module_content.item)

    def test_can_delete_contents_in_module(self):
        self.client.login(**self.credentials)
        module_content = self.create_module_content(content=self.create_text())
        self.client.post(
            (
                reverse(
                    "course:module_content_delete",
                    args=[module_content.module.id],
                )
            )
        )
        self.assertIsNone(module_content.item)

    def test_content_delete_view_redirects_to_module_content_list_page(self):
        self.client.login(**self.credentials)
        module_content = self.create_module_content(content=self.create_text())
        response = self.client.post(
            (
                reverse(
                    "course:module_content_delete",
                    args=[module_content.module.id],
                )
            )
        )
        self.assertRedirects(response, "/course/module/1/")
