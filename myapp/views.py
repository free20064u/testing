from django.shortcuts import render

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
