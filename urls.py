from django.contrib import admin
from django.urls import path
from PetNowApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prestador/',views.prestador, name='prestador'),
    path('usuario/', views.usuario, name='usuario'),
    path('about/', views.about, name='about'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('contacto/', views.contacto, name='contacto'),
    path('beneficios/', views.beneficios, name='beneficios'),
    path('privacidad/', views.privacidad, name='privacidad')
]
