from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from buscador.models import Animal, Imagen, Picture

def index(request):
	mascotas_list = Animal.objects.order_by('-fecha_publicacion')
	context = {'mascotas_list': mascotas_list}
	return render(request, 'buscador/index.html', context) 

def mascota(request, animal_id):
	animal = get_object_or_404(Animal, pk=animal_id)
	return render(request, 'buscador/mascota.html', {'animal': animal})

def nosotros(request):
	context = {}
	return render(request, 'buscador/nosotros.html', context) 


