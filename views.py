from django.shortcuts import render, HttpResponseRedirect
from PetNowApp.forms import RegistroForm, RegistroFormUsuario, ContactForm
from PetNowApp.models import Registro, RegistroUsuario


# Create your views here.

def inicio(request):
      resultados = []

      if request.method == 'POST':
        search_term = request.POST.get('search', '')
        resultados = Registro.objects.filter(categoria__icontains=search_term)|Registro.objects.filter(direccion__icontains=search_term)|Registro.objects.filter(direccionnombre_comercial__icontains=search_term)

      context = {
        'resultados': resultados,
    }

      return render(request, 'PetNowApp/index.html', context)

def usuario(request):
    if request.method == 'POST':
        form= RegistroFormUsuario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('PetNowApp/index.html')
    else:
        form = RegistroForm()
    return render(request, 'PetNowApp/index.html', {'form': form})
        
            

def prestador(request):      
    if request.method == 'POST':
        form= RegistroForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistroForm()
    return render(request, 'PetNowApp/prestador.html', {'form': form})
        
   


def about(request):
    return render(request, 'PetNowApp/about.html')

def mision(request):
    return render(request, 'PetNowApp/mision.html')

def vision(request):
    return render(request, 'PetNowApp/vision.html')

def contacto(request):
    form =ContactForm()
    return render (request, 'PetNowApp/contacto.html',{'form': form}) 

def beneficios(request):
    return render(request,'PetNowApp/beneficios.html')

def privacidad(request):
    return render(request, 'PetNowApp/privacidad.html')
 