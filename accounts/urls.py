from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('editUser/<int:pk>', views.editUser, name='editUser'),
    path('deleteUser/<int:pk>', views.deleteUser, name="deleteUser"),
    
]