from django.shortcuts import render,redirect
from .forms import ElementoForm; 



# Create your views here.

def Articulos(request):
    if request.method == 'POST':
        form = ElementoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el elemento en la base de datos
            return redirect('articulos.html')  # Redirige a una página de éxito o a donde desees

    else:
        form = ElementoForm()

    return render(request, 'articulos.html', {'form': form})
    