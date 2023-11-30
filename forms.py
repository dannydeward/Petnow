from django import forms
from django.forms import ModelForm
from .models import Registro,RegistroUsuario

# Lista de provincias de Argentina
PROVINCIAS_CHOICES = [
    ('Buenos Aires', 'Buenos Aires'),
    ('Catamarca', 'Catamarca'),
    ('Chaco', 'Chaco'),
    ('Chubut', 'Chubut'),
    ('Córdoba', 'Córdoba'),
    ('Corrientes', 'Corrientes'),
    ('Entre Ríos', 'Entre Ríos'),
    ('Formosa', 'Formosa'),
    ('Jujuy', 'Jujuy'),
    ('La Pampa', 'La Pampa'),
    ('La Rioja', 'La Rioja'),
    ('Mendoza', 'Mendoza'),
    ('Misiones', 'Misiones'),
    ('Neuquén', 'Neuquén'),
    ('Río Negro', 'Río Negro'),
    ('Salta', 'Salta'),
    ('San Juan', 'San Juan'),
    ('San Luis', 'San Luis'),
    ('Santa Cruz', 'Santa Cruz'),
    ('Santa Fe', 'Santa Fe'),
    ('Santiago del Estero', 'Santiago del Estero'),
    ('Tierra del Fuego, Antártida e Islas del Atlántico Sur', 'Tierra del Fuego, Antártida e Islas del Atlántico Sur'),
    ('Tucumán', 'Tucumán'),
]


# Lista de categorías
CATEGORIAS_CHOICES = [
    ('Petshop', 'Petshop'),
    ('Veterinaria', 'Veterinaria'),
    ('Hoteles', 'Hoteles'),
    ('Paseadores', 'Paseadores'),
    ('Cuidadores', 'Cuidadores'),
    ('Atencion 24 horas', 'Atencion 24 horas'),
    ('Mayoristas', 'Mayoristas'),
]

MASCOTA=[
    ('Perro','Perro'),
    ('Gato','Gato'),
    ('Pez','Pez'),
    ('Tortuga','Tortuga'),
    ('Ave','Ave'),
    ('Reptil', 'Reptil'),
    ('Roedor','Roedor'),
]
class RegistroForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre_comercial = forms.CharField(max_length=100)
    clave = forms.CharField(widget=forms.PasswordInput, max_length=200)
    repita_clave = forms.CharField(widget=forms.PasswordInput,max_length=200)
    email = forms.EmailField()#(max_length=200)
    repita_email = forms.EmailField()
    #(max_length=200)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    categoria = forms.ChoiceField(choices=CATEGORIAS_CHOICES)
    provincia = forms.ChoiceField(choices=PROVINCIAS_CHOICES)
  
class RegistroFormUsuario(forms.Form):
    usuario = forms.CharField(max_length=100)
    clave = forms.CharField(widget=forms.PasswordInput)
    repita_clave = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(max_length=200)
    repita_email = forms.EmailField(max_length=200)
    direccion = forms.CharField(max_length=200)
    telefono = forms.CharField(max_length=20)
    mascota = forms.ChoiceField(choices=MASCOTA)
    provincia = forms.ChoiceField(choices=PROVINCIAS_CHOICES)
    
    
    
class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    asunto=forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea, max_length=1000)