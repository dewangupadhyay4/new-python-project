from django.contrib import admin
from django.urls import path
from .views import StudentsListCreate, StudentRetriveUpdateDelete, StudentViewSet


urlpatterns = [
    path('students/', StudentsListCreate.as_view(), name='get_students'),
    path('student/<int:pk>/', StudentRetriveUpdateDelete.as_view(), name='student_details'),
]