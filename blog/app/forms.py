from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.shortcuts import render

from .models import Empleo, Publicacion, Postulante, Detallepostulante, Experiencia, Educacion

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
        model = Postulante
        fields = ['nombre_postulante','apellido_postulante','email_postulante','telefono_postulante','genero_postulante','edad_postulante','ciudad_postulante','direccion_postulante']
        labels = {  
            'nombre_postulante': 'Nombres',
            'apellido_postulante': 'Apellidos', 
            'email_postulante': 'Email', 
            'telefono_postulante': 'Teléfono', 
            'genero_postulante': 'Género', 
            'edad_postulante': 'Edad', 
            'ciudad_postulante': 'Ciudad', 
            'direccion_postulante': 'Dirección'
        }
        widgets = { 
             'nombre_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'email_postulante': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'genero_postulante' : forms.Select(choices=genero.items(), attrs = {'class': 'form-control'}),
            'edad_postulante':  forms.NumberInput(attrs = {'class': 'form-control'}), 
            'ciudad_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
            'direccion_postulante': forms.TextInput(attrs = {'class': 'form-control'}),
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
        fields = ['cargo','empresa','pais','area', 'fecha_inicio', 'fecha_final', 'descripcion']
        labels = {
            'cargo': 'Cargo desempeñado',
            'empresa': 'Nombre de la empresa', 
            'pais': 'País', 
            'area': 'Area de Trabajo', 
            'fecha_inicio': 'Fecha Inicial',
            'fecha_final': 'Fecha Final',
            'descripcion': 'Descripcion del cargo'
        }
        widgets = { 
            'cargo': forms.TextInput(attrs = {'class': 'form-control'}),
            'empresa': forms.TextInput(attrs = {'class': 'form-control'}),
            'pais': forms.TextInput(attrs = {'class': 'form-control'}),
            'area': forms.TextInput(attrs = {'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_final': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control'})
        }


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
