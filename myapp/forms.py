from django import forms
from django.forms import ModelForm, widgets
from .models import Course, ProgramWithCourses, Programs


class Course(ModelForm):
    course_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Course name', 'class':'form-control'}))
    class Meta:
        model = Course
        fields = ['course_name']



class Program(ModelForm):
    program_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Program', 'class':'form-control'}))
    class Meta:
        model = Programs
        fields = ['program_name']


class ProgramWithCourse(ModelForm):
    program_name = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Program', 'class': 'form-control mt-2'}))
    course1 = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Course 1', 'class': 'form-control mt-2'}))
    course2 = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Course 2', 'class': 'form-control mt-2'}))
    course3 = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Course 3', 'class': 'form-control mt-2'}))
    course4 = forms.CharField(label='', widget = forms.TextInput(attrs={'placeholder': 'Course 4', 'class': 'form-control mt-2'}))

    class Meta:
        model = ProgramWithCourses
        fields = ['program_name', 'course1', 'course2', 'course3', 'course4']
