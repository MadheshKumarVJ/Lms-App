from django.test import TestCase
from django.urls import resolve, reverse
from tests.courses.test_model_mixin import Modelmixin
from courses.views import (
    ManageCourseListView,
    CourseDeleteView,
    CourseCreateView,
    CourseUpdateView,
    CourseModuleUpdateView,
    ModuleContentListView,
)


class TestUrls(Modelmixin, TestCase):
    def test_manage_course_listview_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:manage_course_list")).func.view_class,
            ManageCourseListView,
        )

    def test_course_createview_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:create")).func.view_class, CourseCreateView
        )

    def test_course_updateview_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:edit", args=[self.course1.pk])
            ).func.view_class,
            CourseUpdateView,
        )

    def test_course_deleteview_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:delete", args=[self.course1.pk])
            ).func.view_class,
            CourseDeleteView,
        )

    def test_course_module_update_view_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:course_module_update", args=[self.course1.pk])
            ).func.view_class,
            CourseModuleUpdateView,
        )

    def test_module_content_list_view_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:module_content_list", args=[self.course1.pk])
            ).func.view_class,
            ModuleContentListView,
        )
