from django import forms
from .models import Categoria, Elemento


MARCA=[
    ('marcas_perros', 'marcas_perros'),
    ('marcas_gatos', 'marcas_gatos'),
    ('marcas_ratones_hámsters','marcas_ratones_hámsters'),
    ('marcas_tortugas','marcas_tortugas'),
    ('marcas_aves','marcas_aves'),
    ('marcas_anfibios','marcas_anfibios'),
    ('marcas_pez', 'marcas_pez'),
    ('marcas_juguetes','marcas_juguetes'), 
    ('marcas_accesorios', 'marcas_accesorios'),
       
]
 
 
class MarcaForm(forms.ModelForm):
    class Meta:
        model: Categoria
        nombre = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(choices=MARCA),
        widget=forms.CheckboxSelectMultiple,   ) 
    
class ElementoForm(forms.ModelForm):
    class Meta:
        model = Elemento
        fields = ['nombre', 'categoria']
   
   
        
   
        