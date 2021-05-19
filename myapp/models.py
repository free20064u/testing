from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.course_name



class Programs(models.Model):
    program_name = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.program_name


class ProgramWithCourses(models.Model):
    program_name = models.CharField(max_length=100, default='')
    course1 = models.CharField(max_length=100, default='')
    course2 = models.CharField(max_length=100, default='')
    course3 = models.CharField(max_length=100, default='')
    course4 = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"Program:{self.program_name}, Courses:{self.course1}, {self.course2},{self.course3},{self.course4}"