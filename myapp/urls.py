from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('contact/', views.contact, name='contact'),
    path('addcourse/', views.addcourse, name='addcourse'),
    path('addprogram/', views.addprogram, name='addprogram'),
    path('programs/<course>/', views.course , name='course'),
    path('addprogramwithcourse', views.addprogramwithcourse, name='addprogramwithcourse'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('allusers/', views.allusers, name='allusers'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('program/', views.program, name='program'),
    path('subject/', views.subject, name='subject'),
    path('programcourse', views.programcourse, name='programcourse'),
    path('send_gmail', views.send_gmail, name='send_gmail')
]
