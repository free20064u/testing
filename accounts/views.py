from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from myapp.models import ProgramWithCourses, Profile
from myapp.forms import ProfileForm1, ProfileForm2

# Create your views here.
prog = ProgramWithCourses.objects.all()

def register(request):
    
    if request.method == 'POST':
        form1 = ProfileForm1(request.POST)
        form2 = ProfileForm2(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password']
        password2 = request.POST['passwordConfirm']

        if True:
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
            elif len(password1) <= 8:
                messages.error(request, 'Password is weak. Your password should be more than 8 characters')
            elif  password1 != password2 :
                messages.info(request, 'Passwords do not much')
            elif Profile.objects.filter(phone_number=phone_number).exists():
                messages.error(request, 'Phone number is already in use')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1, email=email)
                user.save()
            
                userProfile = Profile.objects.create(phone_number=phone_number, user_id=user.id)
                userProfile.save()

                messages.info(request, 'Registration was successful')
                return HttpResponseRedirect('/accounts/login')
            return HttpResponseRedirect('/accounts/register')
        else:
            messages.error(request, 'Registration failed. Try again')
            return HttpResponseRedirect('/accounts/register')

    else:
        form1 = ProfileForm1()
        form2 = ProfileForm2()
        context = {
            'prog':prog,
            'form1': form1,
            'form2': form2,
        }
        return render(request, 'register.html', context)


def editUser(request, pk=None):
    user = get_object_or_404(User, pk=pk)
    profile = get_object_or_404(Profile, user_id=pk)
    
    if request.method == 'POST':
        form1 = ProfileForm1(request.POST)
        form2 = ProfileForm2(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        if request.POST.get('is_superuser', False):
            admin = True
        else:
            admin = False

        if request.POST.get('is_staff',False) == 'on':
            staff = True
        else:
            staff = False

        if request.POST.get('is_student', False) == 'on':
            student = True
        else:
            student = False

        if request.POST.get('is_active', False) == 'on':
            active = True
        else:
            active = False

        if pk :
            if len(first_name) == 0:
                messages.error(request, 'Provide your first name')
            elif len(last_name) ==0:
                messages.info(request, 'Provide your last name')
            elif user.first_name != first_name:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return HttpResponseRedirect ('/accounts/register')
                pass
            elif len(email) < 6:
                messages.error(request, 'Email field is empty or not accurate') 
            elif user.email != email: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                    return HttpResponseRedirect ('/accounts/register')
                pass
            elif profile.phone_number != phone_number:
                if Profile.objects.filter(phone_number=phone_number).exists():
                    messages.error(request, 'Phone number is already in use')
                    return HttpResponseRedirect ('/accounts/register')
                pass
            else:
                user.first_name = first_name 
                user.last_name = last_name
                user.username = username
                user.email = email
                user.is_superuser = admin
                user.is_staff = staff
                user.is_active = active
                user.save()
                profile.phone_number = phone_number
                profile.is_student = student
                profile.save()

                messages.info(request, 'Update was successful')
                return HttpResponseRedirect('/allusers')
            return HttpResponseRedirect('/accounts/register')
        else:
            messages.error(request, 'Update failed. Try again')
            return HttpResponseRedirect('/accounts/register')

    else:
        form1 = ProfileForm1(instance=user)
        form2 = ProfileForm2(instance=profile)
        context = {
            'prog':prog,
            'form1': form1,
            'form2': form2,
            'pk': pk,
        }
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


def deleteUser(request, pk=None):
    user = User.objects.get(pk=pk)
    user.delete()
    messages.success(request, 'User successfully Removed')
    return HttpResponseRedirect('/allusers')


def logout(request):
    auth.logout(request)
    return redirect('/')
