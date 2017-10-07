from django.contrib import admin

from .models import Animal, Mascota, Color

# Register your models here.
admin.site.register(Animal)
admin.site.register(Mascota)
admin.site.register(Color)
