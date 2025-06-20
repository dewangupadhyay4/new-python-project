from django.contrib import admin
from django.urls import path
from .views import student_details, get_students


urlpatterns = [
    # path('students/', StudentsListCreate.as_view(), name='get_students'),
    # path('student/<int:pk>/', StudentRetriveUpdateDelete.as_view(), name='student_details'),
        path('students/', get_students, name='get_students'),
    path('student/<int:pk>/',student_details , name='student_details'),
]