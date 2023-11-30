from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Elemento(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Crear categorías
categoria_perros = Categoria.objects.create(nombre='Comida para Perros')
categoria_gatos = Categoria.objects.create(nombre='Comida para Gatos')
categoria_ratones_hámsters=Categoria.objects.create(nombre='Comida para Ratones y Hámsters')
categoria_tortugas=Categoria.objects.create(nombre='Comida para Tortugas')
categoria_anfibios=Categoria.objects.create(nombre='Comida para anfibios')
categoria_pez=Categoria.objects.create(nombre='Comida para peces')
categoria_aves=Categoria.objects.create(nombre='Comida para aves')
categoria_juguetes= Categoria.objects.create(nombre="Juguetes")
categoria_accesorios=Categoria.objects.create(nombre='accesorios')


# Crear elementos y asignarlos a categorías
marcas_perros = [
    "Royal Canin",
    "Pro Plan (Purina)",
    "Eukanuba",
    "Dog Chow (Purina)",
    "Old Prince",
    "Vital Can",
    "Sabrositos",
    "Pedigree",
    "Nutra-Nuggets",
    "Dingo",
    "Natura Diet",
    "Excellence",
    "Primera",
    "Savor",
    "Nativa",
    "Fit Formula",
    "Raza",
    "Brit Care",
    "Dog Selection",
    "Máxima",
]

for marca in marcas_perros:
    Elemento.objects.create(categoria=categoria_perros, nombre=marca)

marcas_gatos = [
"Royal Canin",
"Pro Plan (Purina)",
"Cat Chow (Purina)"
"Fancy Feast (Purina)",
"Whiskas",
"Sheba",
"Excellence",
"Nutra-Nuggets",
"Cat Lovers Gold",
"Natura Diet",
"Primera",
"Cat Selection",
"Gati",
"Meow Mix",
"Máxima",
"Nature's Variety Instinct",
"Acana",
"Orijen"
"True Origins",
"Feringa"                     
]

for marca in marcas_gatos:
    Elemento.objects.create(categoria=categoria_gatos, nombre=marca)

marcas_ratones_hámsters=[
"Kaytee",
"Vitakraft",
"JR Farm",
"Bunny Nature",
"F.M. Brown's",
"Living World",
"Versele-Laga",
"ZuPreem",
"Beaphar",
]

for marca in marcas_ratones_hámsters:
    Elemento.objects.create(categoria=categoria_ratones_hámsters, nombre=marca)


marcas_tortugas=[
"Exo Terra",
"Zoomed",
"Sera",
"Tetra ReptoMin",
"Nutrafin"
"JBL",
"Turtlefood",
"Repashy",
"Hikari",
]

for marca in marcas_tortugas:
    Elemento.objects.create(categoria=categoria_tortugas, nombre=marca)

marcas_aves=[
"Versele-Laga",
"Kaytee",
"Vitakraft",
"ZuPreem",
"Harrison's Bird Foods",
"Roudybush",
"Lafeber's",
"Beaphar",
"Quiko", 
]

for marca in marcas_aves:
    Elemento.objects.create(categoria=categoria_aves, nombre=marca)

marcas_anfibios=[
"Exo Terra",
"Zoomed",
"Repashy",
"Josh's Frogs",
"Black Panther Zoological",
"T-Rex",
"Josh's Frogs"
"Zoo Med",
"Fluker's",                      
    
]

for marca in marcas_anfibios:
    Elemento.objects.create(categoria=categoria_anfibios, nombre=marca)


marcas_pez =[
"Tetra",
"Sera",
"Tropical",
"Hikari",
"JBL",
"Ocean Nutrition",
"New Life Spectrum",
"Söchting",
"Prodac",
"Nishikoi" ,  
    
]

for marca in marcas_pez:
    Elemento.objects.create(categoria=categoria_pez, nombre=marca)
    
marcas_juguetes=[
"Pelotas (de tenis, de goma, de cuerda)",
"Juguetes masticables (huesos de nylon, juguetes de caucho)",
"Juguetes interactivos (rompecabezas, dispensadores de premios)",
"Juguetes chirriantes",
"Juguetes de cuerda",
"Frisbees",
"Juguetes para masticar",
"Juguetes rellenos (con sonidos y/o premios)",
"Peluches resistentes",
"Juguetes de tira y afloja",
"Juguetes para buscar y recoger",
"Juguetes para el agua (flotantes y resistentes al agua)",   
"Juguetes con plumas",
"Ratones de juguete",
"Juguetes de peluche",
"Pelotas con campanillas",
"Juguetes láser",
"Juguetes de caña con objetos colgantes",
"Juguetes rellenos con catnip (hierba gatera)",
"Rascadores y postes para gatos",
"Juguetes de papel arrugado",
"Juguetes interactivos electrónicos",
"Túneles y escondites",
"Juguetes para perseguir",
"Pelotas de ping pong",
"Juguetes para trepar y escalar",
"Juguetes para el adiestramiento",
"Juguetes de estimulación mental",
"Juguetes interactivos de alimentación ",  
    
]

for marca in marcas_juguetes:
    Elemento.objects.create(categoria=categoria_juguetes, nombre=marca)
    

marcas_accesorios=[
"Collares y correas",
"Arné",
"Camas y almohadones",
"Ropa y disfraces",
"Platos y comederos",
"Bebederos automáticos",
"Transportadoras y bolsos",
"Cepillos y peines",
"Cinturones de seguridad para el auto",
"GPS y localizadores",
"Chalecos reflectantes",
"Bandanas y accesorios decorativos",
"Ropa y accesorios decorativos",
"Pañales y productos de higiene",   
"Collares con campanillas",
"Rascadores y postes para arañar",
"Camas y cuevas",
"Platos y comederos",
"Areneros y palas",
"Juguetes con catnip",
"Transportadoras y bolsos",
"Fuentes de agua",
"Cepillos y peines",
"lazos",
      
]   
 
for marca in marcas_accesorios:
    Elemento.objects.create(categoria=categoria_accesorios, nombre=marca)   
# Repite el proceso para las otras categorías y elementos