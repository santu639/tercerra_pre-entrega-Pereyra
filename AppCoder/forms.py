from django import forms
from AppCoder.models import Post
from AppCoder.models import Busqueda_Curso
from AppCoder.models import Datos

class PostForm (forms.ModelForm):
    class Meta:
        model = Post
        fields= '__all__'


class CursoForm (forms.ModelForm):
    class Meta:
        model = Busqueda_Curso
        fields= '__all__'

class Datosform (forms.ModelForm):
    class Meta:
        model = Datos
        fields= '__all__'