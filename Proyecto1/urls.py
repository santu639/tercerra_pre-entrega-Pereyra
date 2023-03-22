"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import mostrar_base, mostrar_post, agregar_post, buscar_post, mostrar_curso, agregar_curso, buscar_curso, mostrar_datos, agregar_datos, buscar_datos


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('mis-post/', mostrar_post, name="mis-post"),
    path('mis-post/agregar', agregar_post, name= "agregar-post"),
    path ('mis-post/buscar', buscar_post, name= "buscar-post"),
    path('Curso/', mostrar_curso, name= "Curso"),
    path('Curso/Agregar', agregar_curso, name= "agregar-curso"),
    path('Curso/buscar', buscar_curso, name= "buscar-Curso"),
    path('Datos/', mostrar_datos, name= "Datos"),
    path('Datos/Agregar', agregar_datos, name= "agregar-datos"),
    path('Datos/buscar', buscar_datos, name= "buscar-datos"),
    path ('', mostrar_base, name= "inicio"),
]
