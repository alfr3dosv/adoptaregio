# AdoptaRegio - Hackathon FCFM 2017

Adopta Regio es una aplicación opensource para las organizaciones dedicadas a la adopcion de perros y gatos.

## Requisitos

* Python 2
* Python 3
* Django >= 1.8

### Ubuntu server
```
sudo apt install python-dev python-django
```
## Setup

### Puesta en marcha

 1. Clonar el repositorio
 ```
 git clone https://github.com/alfr3dosv/adoptaregio.git
 ```
 
 2. Seleccionar la carpeta
 ```
 cd adoptaregio.git
 ``` 

 3. Iniciar
 ```
 python3 manage.py runserver
 ```

El sitio se encuentra en ``http://127.0.0.1:8000/buscador/ ``

### Administrador

Para entrar en la pagina de administración ``http://127.0.0.1:8000/admin``

Usuario por defecto:**alfredo**

Contraseña por defecto:**password**

### Limpiar base de datos

Limpiar la base de datos, incluyendo usuarios
```
python manage.py flush
```

Tendras que crear un nuevo superusuario
```
python mage.py createsuperuser
```
### Desplegar en un servidor

Recomendamos [Heroku](https://www.heroku.com/) y seguir esta [guia](https://devcenter.heroku.com/articles/deploying-python).

## Autores

* Alfredo Soto
* Israel L. Garcia
* Estefani Oviedo
