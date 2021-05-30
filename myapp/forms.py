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
    programs = forms.ModelChoiceField(queryset=Programs.objects.all().order_by('program_name'), widget=forms.Select(attrs={'placeholder':'Program', 'class':'form-control'}))
    course1 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course1', 'class':'form-control'}))
    course2 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course2', 'class':'form-control'}))
    course3 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course3', 'class':'form-control'}))
    course4 = forms.ModelChoiceField(queryset=Courses.objects.all().order_by('course_name'),widget=forms.Select(attrs={'placeholder':'Course4', 'class':'form-control'}))
   

    class Meta:
        model = ProgramWithCourses
        fields = ['programs', 'course1', 'course2', 'course3', 'course4']
