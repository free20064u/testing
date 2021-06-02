import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Courses, Programs, ProgramWithCourses
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import Course, Program, ProgramWithCourse
from twilio.rest import Client

# Create your views here.
def prog():
    prog = ProgramWithCourses.objects.all().order_by('programs')
    return prog



def index(request):
    context = {
        'prog': prog
    }
    return render(request, 'index.html', context)


def programs(request):
    context = {
        'programs': prog,
        'prog': prog,
    }
    return render(request, 'programs.html', context)


def contact(request):
    context = {
        'prog': prog
    }
    return render(request, 'contact.html', context)


def course(request, course=None):
    core_courses = ['English', 'Integrated science', 'Mathematics', 'Social Studies']
    courseID = get_object_or_404(Programs, program_name = course)
    program_with_courses = get_object_or_404(ProgramWithCourses, programs=courseID.id)
    if program_with_courses is not None:
        course = course
        context = {
            'prog': prog,
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
        return redirect('subject')
    else:   
        form = Course()
        context = {
            'prog': prog,
            'form': form
        }
        return render(request, 'addcourse.html', context)


def addprogram(request):
    if request.method == 'POST':
        form = Program(request.POST)
        form.is_valid()
        form.save()
        messages.success(request, 'Program was added succesfully')
        return redirect('program')
    else:
        form = Program()
        context = {
            'prog': prog,
            'form': form
        }
        return render(request, 'addcourse.html', context)


def addprogramwithcourse(request):
    if request.method == 'POST':
        form = ProgramWithCourse(request.POST)
        form.is_valid()
        form.save()
        messages.success(request, 'Program with course was add succefully')
        return redirect('programcourse')
    else:
        form = ProgramWithCourse()
        context = {
            'prog': prog,
            'form': form
        }
        return render(request, 'addcourse.html', context)

def dashboard(request):
    context = {
        'prog': prog
    }
    return redirect('allusers')


def allusers(request):
    users = User.objects.all().order_by('username')
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)

def teachers(request):
    users = User.objects.filter(is_staff__exact=1).order_by()
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)

def students(request):
    users = User.objects.filter(is_staff__exact = 0).order_by('username')
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)


def program(request):

    programs = Programs.objects.all().order_by('program_name')
    
    context = {
        'prog': prog,
        'programs': programs
    }
    return render(request, 'dashboard.html', context)


def subject(request):
    subjects = Courses.objects.all().order_by('course_name')

    
    context = {
        'prog': prog,
        'subjects': subjects,
    }
    return render(request, 'dashboard.html', context)


def programcourse(request):
    programcourses = ProgramWithCourses.objects.all().order_by('programs_id')
    context = {
        'prog': prog,
        'programcourses': programcourses
    }
    return render(request, 'dashboard.html', context)


def send_gmail(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        #message = f'Thanks {name}, your message has been recieved. we will get back to you very soon'
        from_email = 'free20064u@gmail.com'


        #sending an email to customer
        send_mail(subject, message, from_email, [email], fail_silently=True)

        #sending a text message to customer
        account_sid = 'get from twilo'
        auth_token = 'get from twilo'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                              body= message,
                              from_='+16466797538',
                              to= phone,
                          )

        return render(request, 'contact.html')


def editprogram(request):
    if request.method == "POST":
        pk = request.POST['pk']
        program = get_object_or_404(Programs, pk=pk)
        form = Program(request.POST, instance=program)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/program')
    else:
        pk = request.GET['pk']
        program = get_object_or_404(Programs, pk=pk)
        form = Program(instance=program)
        context = {
            'form': form,
            'prog': prog,
            'pk': pk
        }
        return render(request, 'addcourse.html', context)

