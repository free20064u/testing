from django.contrib import admin
from .models import Program, Course, ProgramWithCourses


# Register your models here.
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(ProgramWithCourses)
