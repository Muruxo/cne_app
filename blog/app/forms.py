from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Empleo, Publicacion, Experiencia, Educacion

MODALIDAD_EMPLEO_CHOICES = ["Activado", "Desactivado", "Pendiente"]

class EmpleoForm(ModelForm):
    class Meta: 
        model = Empleo
        fields = '__all__'
        labels = {
            'nombre_empleo': 'Empleo', 
            'descripcion_empleo' : 'Descripción',
            'fecha_empleo': 'Fecha de Publicación',
            'area_empleo': 'Area del Empleo',
            'modalidad_empleo': 'Modalidad de Trabajo',
            'tiempo_empleo': 'Tiempo de contrato',
            'id_ciudad_fk': 'Ciudad',
            
        }
        widgets = {
            'nombre_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'descripcion_empleo': forms.Textarea(attrs = {'class': 'form-control'}),
            'fecha_empleo':forms.DateInput(attrs={'class': 'form-control', 'display':'center' }),
            'area_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'modalidad_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'tiempo_empleo':forms.TextInput(attrs= {'type': 'number', 'class': 'form-control'}),
            'id_ciudad_fk':forms.TextInput(attrs = {'class': 'form-control'}),
        }
        
class PublicacionForm(ModelForm):
    class Meta: 
        model = Publicacion
        fields = '__all__'
        labels = {
            'titulo': 'Empleo', 
            'descripcion' : 'Descripción',
            'email': 'Email',
        }
        widgets = {
            'titulo': forms.TextInput(attrs = {'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
        }
        

class DatosPersonalesForm(forms.ModelForm):
    class Meta: 
        genero = {'M':'Masculino', 'F':'Femenino'}
        model = User
        fields = ['first_name','last_name','email','telefono','genero','edad','ciudad','direccion']
        labels = {  
            'first_name': 'Nombres',
            'last_name': 'Apellidos', 
            'email': 'Email', 
            'telefono': 'Teléfono', 
            'genero': 'Género', 
            'edad': 'Edad', 
            'ciudad': 'Ciudad', 
            'direccion': 'Dirección'
        }
        widgets = { 
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control'}),
            'genero' : forms.Select(choices=genero.items(), attrs = {'class': 'form-control'}),
            'edad':  forms.NumberInput(attrs = {'class': 'form-control'}), 
            'ciudad': forms.TextInput(attrs = {'class': 'form-control'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
        }

# class DatosAdicionalesForm(ModelForm):
#     class Meta: 
#         model = Detallepostulante
#         fields = ['descripcion_laboral','idioma_laboral']
#         labels = {
#             'descripcion_laboral': 'Descripcion', 
#             'idioma_laboral': 'Idioma', 
#         }
#         widgets = { 
#             'descripcion_laboral': forms.Textarea(attrs = {'class': 'form-control'}),
#             'idioma_laboral': forms.NumberInput(attrs = {'class': 'form-control'}),
#         }


class ExperienciaForm(forms.ModelForm):
    class Meta: 
        model = Experiencia
        fields = ['cargo','empresa','pais','area', 'fecha_inicio', 'fecha_final', 'descripcion', 'curriculum']
        labels = {
            'cargo': 'Cargo desempeñado',
            'empresa': 'Nombre de la empresa', 
            'pais': 'País', 
            'area': 'Area de Trabajo', 
            'fecha_inicio': 'Fecha Inicial',
            'fecha_final': 'Fecha Final',
            'descripcion': 'Descripcion del cargo',
            'curriculum' : 'Subir Curriculum Vitae'
        }
        widgets = { 
            'cargo': forms.TextInput(attrs = {'class': 'form-control'}),
            'empresa': forms.TextInput(attrs = {'class': 'form-control'}),
            'pais': forms.TextInput(attrs = {'class': 'form-control'}),
            'area': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_final': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control'}),
            'curriculum': forms.FileInput(attrs = {'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postulante'] = forms.CharField(widget=forms.HiddenInput())


class EducacionForm(forms.ModelForm):
    class Meta: 
        estado = {'1':'En Curso', '2':'Graduado', '3':'Abandonado'}
        model = Educacion
        fields = ['titulo_edu','pais_edu','institucion_edu','nivel_edu', 'estado_edu', 'descripcion_edu']
        labels = {
            'titulo_edu': 'Titulo',
            'pais_edu': 'Pais', 
            'institucion_edu': 'Institucion', 
            'nivel_edu': 'Area', 
            'estado_edu': 'Estado',
            'descripcion_edu': 'Descripcion',
        }
        widgets = { 
            'titulo_edu': forms.TextInput(attrs = {'class': 'form-control'}),
            'pais_edu': forms.TextInput(attrs = {'class': 'form-control'}),
            'institucion_edu': forms.TextInput(attrs = {'class': 'form-control'}),
           'nivel_edu': forms.Select(attrs = {'class': 'form-control'}),
            'estado_edu': forms.Select(choices=estado.items(), attrs = {'class': 'form-control'}),
            'descripcion_edu': forms.TextInput(attrs = {'class': 'form-control'})
        }
