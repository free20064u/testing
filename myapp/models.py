import os
from twilio.rest import Client
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=200, default='', blank=True)
    is_student = models.BooleanField(default=False)


    def __str__(self):
        return self.user


class Courses(models.Model):
    course_name = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.course_name



class Programs(models.Model):
    program_name = models.CharField(max_length=100, default='')
    
    class Meta:
        ordering = ['program_name']

    def __str__(self):
        return self.program_name


class ProgramWithCourses(models.Model):
    programs = models.ForeignKey(Programs, null=True, on_delete=models.CASCADE)

    course1 = models.CharField(max_length=100, default='')
    course2 = models.CharField(max_length=100, default='')
    course3 = models.CharField(max_length=100, default='')
    course4 = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['programs']


    def __str__(self):
        return f"Program:{self.programs}, Course1:{self.course1}"


    
    
