from django.db import models

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

class Registro(models.Model):
    usuario = models.CharField(max_length=100)
    nombre_comercial = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)  # No es recomendable almacenar contraseñas en texto plano. Considera usar un campo de tipo PasswordField
    repita_clave = models.CharField(max_length=100)  # No es recomendable almacenar contraseñas en texto plano. Considera usar un campo de tipo PasswordField
    email = models.EmailField()
    repita_email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    categoria = models.CharField(choices=CATEGORIAS_CHOICES, max_length=100)

# Create your models here.
class RegistroUsuario(models.Model):
    usuario = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)  # No es recomendable almacenar contraseñas en texto plano. Considera usar un campo de tipo PasswordField
    repita_clave = models.CharField(max_length=100)  # No es recomendable almacenar contraseñas en texto plano. Considera usar un campo de tipo PasswordField
    email = models.EmailField()
    repita_email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    mascota = models.CharField(choices=MASCOTA, max_length=100)
    provincia = models.CharField(choices=PROVINCIAS_CHOICES, max_length=100)