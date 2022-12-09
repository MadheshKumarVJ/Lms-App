from django.test import TestCase
from django.urls import resolve, reverse
from tests.courses.test_model_mixin import Modelmixin
from courses.views import (
    ManageCourseListView,
    CourseDeleteView,
    CourseCreateView,
    CourseUpdateView,
)


class TestUrls(Modelmixin, TestCase):
    def test_Manage_Course_ListView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:manage_course_list")).func.view_class,
            ManageCourseListView,
        )

    def test_Course_CreateView_is_resolved(self):
        self.assertEqual(
            resolve(reverse("course:create")).func.view_class, CourseCreateView
        )

    def test_Course_UpdateView_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:edit", args=[self.course1.pk])
            ).func.view_class,
            CourseUpdateView,
        )

    def test_Course_DeleteView_is_resolved(self):
        self.assertEqual(
            resolve(
                reverse("course:delete", args=[self.course1.pk])
            ).func.view_class,
            CourseDeleteView,
        )
