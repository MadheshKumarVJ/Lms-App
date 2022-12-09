from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    path(
        "mine/",
        views.ManageCourseListView.as_view(),
        name="manage_course_list",
    ),
    path("create/", views.CourseCreateView.as_view(), name="create"),
    path("<pk>/edit/", views.CourseUpdateView.as_view(), name="edit"),
    path("<pk>/delete/", views.CourseDeleteView.as_view(), name="delete"),
    path(
        "<pk>/module/",
        views.CourseModuleUpdateView.as_view(),
        name="module_update",
    ),
]
