from django.shortcuts import render, get_object_or_404, redirect
from .models import Program, ProgramWithCourses
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    return render(request, 'index.html')


def programs(request):
    programs = Program.objects.all()
    
    context = {
        'programs': programs
    }
    return render(request, 'programs.html', context)


def contact(request):
    return render(request, 'contact.html')


def course(request, course=None):
    core_courses = ['English', 'Integrated science', 'Mathematics', 'Social Studies']
    program_with_courses = get_object_or_404(ProgramWithCourses, program_name=course)
    course = course
    context = {
        'course': course,
        'core_courses': core_courses,
        'program_with_courses': program_with_courses
    }
    return render(request, 'course.html', context)
