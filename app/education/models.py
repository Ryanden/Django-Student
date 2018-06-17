from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    author = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
