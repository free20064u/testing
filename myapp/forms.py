from django import forms
from django.forms import ModelForm, widgets
from .models import Course, Program, ProgramWithCourses


class Course(ModelForm):
    course_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Course name', 'class':'form-control'}))
    class Meta:
        model = Course
        fields = ['course_name']



class Program(ModelForm):
    program_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Program', 'class':'form-control'}))
    class Meta:
        model = Program
        fields = ['program_name']

