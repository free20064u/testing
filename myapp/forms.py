from django import forms
from django.forms import ModelForm, widgets
from django.contrib.auth.models import User
from .models import Courses, ProgramWithCourses, Programs, Profile

class ProfileForm1(ModelForm):
    first_name = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    username = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    email = forms.CharField(label='', widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    passwordConfirm = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirm', 'class': 'form-control'}))
    

    class Meta:
        
        model = User
        fields = ['first_name', 'last_name','username', 'email','is_superuser', 'password']

class ProfileForm2(ModelForm):
    phone_number = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    is_student = forms.BooleanField(required=False)
    
    class Meta:
        model = Profile
        fields = ['phone_number', 'is_student']



class Course(ModelForm):
    course_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Course name', 'class':'form-control'}))
    class Meta:
        model = Courses
        fields = ['course_name']



class Program(ModelForm):
    program_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Program', 'class':'form-control'}))
    class Meta:
        model = Programs
        fields = ['program_name']


class ProgramWithCourse(ModelForm):
    programs = forms.ModelChoiceField(queryset=Programs.objects.all().order_by('program_name'), widget=forms.Select(attrs={'placeholder':'Program', 'class':'form-control'}))
    course1 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course1', 'class':'form-control'}))
    course2 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course2', 'class':'form-control'}))
    course3 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course3', 'class':'form-control'}))
    course4 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course4', 'class':'form-control'}))
   

    class Meta:
        model = ProgramWithCourses
        fields = ['programs', 'course1', 'course2', 'course3', 'course4']
