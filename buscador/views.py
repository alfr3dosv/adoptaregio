from django.shortcuts import render
from django.http import HttpResponse
from buscador.models import Animal

def index(request):
	mascotas_list = Animal.objects.order_by('-fecha_publicacion')
	context = {'mascotas_list': mascotas_list}
	return render(request, 'buscador/index.html', context) 