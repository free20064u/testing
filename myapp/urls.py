from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs, name='programs'),
    path('contact/', views.contact, name='contact'),
    path('programs/<course>/', views.course , name='course')
]
