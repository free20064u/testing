from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')


def programs(request):
    programs = ['General Science', 'Agricultural science', 'Business','General Arts', 'Home Economics', 'Visual Arts']
    
    context = {
        'programs': programs
    }
    return render(request, 'programs.html', context)


def contact(request):
    return render(request, 'contact.html')


def course(request, course=None):
    course = course
    context = {
        'course': course
    }
    return render(request, 'course.html', context)
