from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nosotros/$', views.nosotros, name='nosotros'),
    url(r'^(?P<animal_id>[0-9]+)/$', views.mascota, name='mascota'),
]