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
# Getting list of programs from the database
def prog():
    prog = ProgramWithCourses.objects.all().order_by('programs')
    return prog


# View for the displaying the homepage
def index(request):
    context = {
        'prog': prog
    }
    return render(request, 'index.html', context)

# View for displaying programs offered by school
def programs(request):
    context = {
        'programs': prog,
        'prog': prog,
    }
    return render(request, 'programs.html', context)

# View for displaying contact and map page for the school
def contact(request):
    context = {
        'prog': prog
    }
    return render(request, 'contact.html', context)

# View for displaying details about the programs offered by the school
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

#Adding courses or subjects to the database
def addcourse(request):
    if request.method == 'POST':
        form = Course(request.POST)
        form.is_valid()
        form.save()
        messages.success(request, 'Course has been added succesfully')
        return redirect('subject')
    else:   
        form = Course()
        context = {
            'prog': prog,
            'form': form
        }
        return render(request, 'addcourse.html', context)

#Adding programs to the database
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

#Adding programs and their respective subject or courses
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
        

#Displays all users in the database on dashboard
def allusers(request):
    users = User.objects.all().order_by('username')
    messages.info(request, 'All users')
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)

#Displays users who are teachers 
def teachers(request):
    users = User.objects.filter(is_staff__exact=1).order_by()
    messages.info(request, 'All Teachers')
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)

#Displays users who are students
def students(request):
    users = User.objects.filter(is_staff__exact = 0).order_by('username')
    messages.info(request, 'All Students')
    context = {
        'prog': prog,
        'users': users
    }
    return render(request, 'dashboard.html', context)

#Displays programs in the database to the admin
def program(request):

    programs = Programs.objects.all().order_by('program_name')
    messages.info(request, 'All Programs')
    
    context = {
        'prog': prog,
        'programs': programs
    }
    return render(request, 'dashboard.html', context)

#Displayes subjects or courses to the admin
def subject(request):
    subjects = Courses.objects.all().order_by('course_name')
    messages.info(request, 'All Subject')

    
    context = {
        'prog': prog,
        'subjects': subjects,
    }
    return render(request, 'dashboard.html', context)

#Displays programs and their respective courses or subject to the admin
def programcourse(request):
    programcourses = ProgramWithCourses.objects.all().order_by('programs_id')
    messages.info(request, 'All programs with courses')
    context = {
        'prog': prog,
        'programcourses': programcourses
    }
    return render(request, 'dashboard.html', context)

#Sends email and text message to the user who filled contact forms
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

#Updating of programs allready in the database
def editprogram(request):
    if request.method == "POST":
        pk = request.POST['pk']
        program = get_object_or_404(Programs, pk=pk)
        form = Program(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program has been successfully updated')
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

#Updationg of courses allready in the database
def editcourse(request):
    if request.method == "POST":
        pk = request.POST['pk']
        course = get_object_or_404(Courses, pk=pk)
        form = Course(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject has been successfully updated')
            return HttpResponseRedirect('/subject')
    else:
        pk = request.GET['pk']
        course = get_object_or_404(Courses, pk=pk)
        form = Course(instance=course)
        context = {
            'form': form,
            'prog': prog,
            'pk': pk
        }
        return render(request, 'addcourse.html', context)


#Update program with courses already in database
def editprogramwithcourse(request):
    if request.method == "POST":
        pk = request.POST['pk']
        programwithcourse = get_object_or_404(ProgramWithCourses, pk=pk)
        form = ProgramWithCourse(request.POST, instance=programwithcourse)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program with course has been successfully updated')
            return HttpResponseRedirect('/programcourse')
    else:
        pk = request.GET['pk']
        programwithcourse = get_object_or_404(ProgramWithCourses, pk=pk)
        form = ProgramWithCourse(instance=programwithcourse)
        context = {
            'form': form,
            'prog': prog,
            'pk': pk
        }
        return render(request, 'addcourse.html', context)