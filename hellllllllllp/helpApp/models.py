from django.db import models

class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name
