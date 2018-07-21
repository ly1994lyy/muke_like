from django.urls import path
from .views import CourseListView, CourseDetailView

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
]