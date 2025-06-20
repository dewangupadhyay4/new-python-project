from django.contrib import admin
from django.urls import path
from .views import student_details, get_students


urlpatterns = [
    # path('students/', StudentsListCreate.as_view(), name='get_students'),
    # path('student/<int:pk>/', StudentRetriveUpdateDelete.as_view(), name='student_details'),
        path('students/', student_details, name='get_students'),
    path('student/<int:pk>/', get_students, name='student_details'),
]