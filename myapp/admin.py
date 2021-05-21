from django.contrib import admin
from .models import Programs, Courses, ProgramWithCourses


# Register your models here.
admin.site.register(Programs)
admin.site.register(Courses)
admin.site.register(ProgramWithCourses)
