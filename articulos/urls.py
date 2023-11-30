from django.contrib import admin
from django.urls import path
from articulos import views

urlpatterns = [
    path('articulos/', views.Articulos, name='articulos '),
   
]