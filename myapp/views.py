from django.shortcuts import render, get_object_or_404, redirect
from .models import Programs, ProgramWithCourses
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import Course, Program, ProgramWithCourse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def programs(request):
    programs = ProgramWithCourses.objects.all()
    
    context = {
        'programs': programs
    }
    return render(request, 'programs.html', context)


def contact(request):
    return render(request, 'contact.html')


def course(request, course=None):
    core_courses = ['English', 'Integrated science', 'Mathematics', 'Social Studies']
    courseID = get_object_or_404(Programs, program_name = course)
    program_with_courses = get_object_or_404(ProgramWithCourses, programs=courseID.id)
    if program_with_courses is not None:
        course = course
        context = {
            'course': course,
            'core_courses': core_courses,
            'program_with_courses': program_with_courses
        }
        return render(request, 'course.html', context)
    else:
        messages.info(request, 'Cousrse does not exist')
        return render(request, 'course.html')


def addcourse(request):
    if request.method == 'POST':
        form = Course(request.POST)
        form.is_valid()
        form.save()
        messages.info(request, 'Course has been added succesfully')
        return render(request, 'addcourse.html')
    else:   
        form = Course()
        context = {
        'form': form
        }
        return render(request, 'addcourse.html', context)


def addprogram(request):
    if request.method == 'POST':
        form = Program(request.POST)
        form.is_valid()
        form.save()
        messages.success(request, 'Program was added succesfully')
        return render(request, 'addcourse.html')
    else:
        form = Program()
        context = {
        'form': form
        }
        return render(request, 'addcourse.html', context)


def addprogramwithcourse(request):
    if request.method == 'POST':
        form = ProgramWithCourse(request.POST)
        form.is_valid()
        form.save()
        messages.success(request, 'Program with course was add succefully')
        return render(request, 'addcourse.html')
    else:
        form = ProgramWithCourse()
        context = {
            'form': form
        }
        return render(request, 'addcourse.html', context)

def dashboord(request):
    return render(request, 'dashboard.html')


def allusers(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard.html', context)

def teachers(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard.html', context)
