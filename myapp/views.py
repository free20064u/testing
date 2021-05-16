from django.shortcuts import render, get_object_or_404
from .models import Program

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
    program = get_object_or_404(Program, course=course)
    course = course
    context = {
        'course': course,
        'program': program
    }
    return render(request, 'course.html', context)
