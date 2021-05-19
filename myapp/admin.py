from django.contrib import admin
from .models import Programs, Course, ProgramWithCourses


# Register your models here.
admin.site.register(Programs)
admin.site.register(Course)
admin.site.register(ProgramWithCourses)
