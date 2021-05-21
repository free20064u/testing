from django import forms
from django.forms import ModelForm, widgets
from .models import Courses, ProgramWithCourses, Programs


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
    program_name = forms.ModelChoiceField(queryset=Programs.objects.all(), widget=forms.Select(attrs={'placeholder':'Program', 'class':'form-control'}))
    course = forms.ModelChoiceField(queryset=Courses.objects.all(),widget=forms.Select(attrs={'placeholder':'Program', 'class':'form-control'}))
   

    class Meta:
        model = ProgramWithCourses
        fields = ['program_name', 'course']
