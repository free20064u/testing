from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
from myapp.models import ProgramWithCourses

# Create your views here.
prog = ProgramWithCourses.objects.all()

def register(request):
    context = {
        'prog':prog
    }

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirmPass = request.POST['password2']

        if len(first_name) == 0:
            messages.info(request, 'Provide your first name')
        elif len(last_name) ==0:
            messages.info(request, 'Provide your last name')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
        elif len(email) == 0:
            messages.info(request, 'Email field is empty')    
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already taken')
        elif  password1 != confirmPass :
            messages.info(request, 'Passwords do not much')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
            user.save()
            messages.info(request, 'Registration was successful')
            
        return render(request, 'register.html', context)

    else:
        return render(request, 'register.html', context)

def login(request):
    context = {
        'prog': prog
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid password')
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
