from django.contrib import admin

from .models import Animal, Mascota, Color, Imagen, Picture

# Register your models here.
admin.site.register(Animal)
admin.site.register(Mascota)
admin.site.register(Color)
admin.site.register(Imagen)
admin.site.register(Picture)
