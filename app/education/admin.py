from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import School, Student

admin.site.register(School)
admin.site.register(Student)
