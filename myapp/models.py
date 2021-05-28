from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.course_name



class Programs(models.Model):
    program_name = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.program_name


class ProgramWithCourses(models.Model):
    programs = models.ForeignKey(Programs, null=True, on_delete=models.PROTECT)

    course1 = models.CharField(max_length=100, default='')
    course2 = models.CharField(max_length=100, default='')
    course3 = models.CharField(max_length=100, default='')
    course4 = models.CharField(max_length=100, default='')


    def __str__(self):
        return f"Program:{self.programs}, Course1:{self.course1}"