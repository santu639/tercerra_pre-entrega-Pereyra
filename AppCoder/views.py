from django.shortcuts import render
from AppCoder.models import Post
from AppCoder.forms import PostForm
from AppCoder.models import Busqueda_Curso
from AppCoder.forms import CursoForm
from AppCoder.forms import Datosform
from AppCoder.models import Datos

# Create your views here.
def mostratr_otro_template(request):
    posts = Post.objects.all()
    return render (request, "AppCoder/otro_template.html", {"posts": posts})


def index (request):
    return render(request, "AppCoder/index.html")

def mostrar_post(request):
    
    context= {
        "form": PostForm(),
        "posts": Post.objects.all(),

    }
    return render(request, "AppCoder/admin_post.html", context)

def agregar_post (request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
        "form": PostForm(),
        "posts": Post.objects.all(),
    }
    return render (request, "AppCoder/admin_post.html", context)

def buscar_post(request):
    criterio= request.GET.get("criterio")
    context = {
        "posts": Post.objects.filter(Nombre__icontains=criterio).all(),
    }
    return render (request, "AppCoder/admin_post.html", context)
#--------------------------------------------------------------------------

def mostrar_curso(request):
    
    context= {
        "form": CursoForm(),
        "cursos": Busqueda_Curso.objects.all(),

    }
    return render(request, "AppCoder/Curso.html", context)

def agregar_curso (request):

    curso_form = CursoForm(request.POST)

    curso_form.save()
    
    context = {
        
        "form": CursoForm(),
        "cursos": Busqueda_Curso.objects.all(),
        
    }
    return render (request, "AppCoder/Curso.html", context)

def buscar_curso(request):
    criterio= request.GET.get("criterio")
    context = {
        "cursos": Busqueda_Curso.objects.filter(Curso__icontains=criterio).all(),
    }
    return render (request, "AppCoder/Curso.html", context)

#-------------------------------------------------
def mostrar_datos(request):
    
    context= {
        "form": Datosform(),
        "datos": Datos.objects.all(),

    }
    return render(request, "AppCoder/datos.html", context)

def agregar_datos (request):

    datos_form = Datosform(request.POST)

    datos_form.save()
    
    context = {
        
        "form": Datosform(),
        "datos": Datos.objects.all(),
        
    }
    return render (request, "AppCoder/datos.html", context)

def buscar_datos(request):
    criterio= request.GET.get("criterio")
    context = {
        "datos": Datos.objects.filter(Pais__icontains=criterio).all(),
    }
    return render (request, "AppCoder/datos.html", context)

#----------------------------------------------------
def mostrar_base(request):
      
       return render (request, "AppCoder/Base.html")

