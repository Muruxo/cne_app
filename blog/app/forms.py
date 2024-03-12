from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.core.validators import RegexValidator
from datetime import datetime

MODALIDAD_EMPLEO_CHOICES = ["Activado", "Desactivado", "Pendiente"]

fecha_actual = datetime.now().strftime('%Y-%m-%d')

def validar_pdf(value):
    import os
    from django.core.exceptions import ValidationError

    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    if ext.lower() != '.pdf':
        raise ValidationError('Solo se permiten archivos PDF.')
    

class EmpleoForm(ModelForm):
    class Meta: 
        model = Empleo
        fields = ['nombre_empleo','descripcion_empleo','fecha_empleo','area_empleo','modalidad_empleo','tiempo_empleo','id_ciudad_fk']
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
            'fecha_empleo':forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control', 'max': fecha_actual}),
            'area_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'modalidad_empleo': forms.TextInput(attrs = {'class': 'form-control'}),
            'tiempo_empleo':forms.NumberInput(attrs = {'class': 'form-control', 'min': '1', 'max': '99'}),
            'id_ciudad_fk':forms.Select(attrs = {'class': 'form-control'}),
           
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
        genero = {'':'- Seleccione -','M':'Masculino', 'F':'Femenino'}
        model = Postulante
        fields = ['nombre','apellido','email','telefono','genero','edad','ciudad','direccion']
        labels = {  
            'nombre': 'Nombres',
            'apellido': 'Apellidos', 
            'email': 'Email', 
            'telefono': 'Teléfono', 
            'genero': 'Género', 
            'edad': 'Edad', 
            'ciudad': 'Ciudad', 
            'direccion': 'Dirección',
        }
        widgets = { 
            'nombre': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'telefono': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '[0-9]+', 'title': 'Por favor, ingrese solo números'}),
            'genero' : forms.Select(choices=genero.items(), attrs = {'class': 'form-control'}),
            'edad':  forms.NumberInput(attrs = {'class': 'form-control', 'min': '18', 'max': '99'}), 
            'ciudad': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'direccion': forms.TextInput(attrs = {'class': 'form-control'}),
        }
    

class CurriculumForm(forms.ModelForm):
    class Meta: 
        model = Postulante
        fields = ['curriculum']
        labels = {  
            'curriculum' : 'Subir Curriculum Vitae (en PDF)'
        }
        widgets = { 
            'curriculum': forms.FileInput(attrs = {'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['curriculum'].validators.append(validar_pdf)
        self.fields['curriculum'].widget.attrs.update({'accept': 'application/pdf'})


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
        fields = ['cargo','empresa','pais','area', 'fecha_inicio', 'fecha_final', 'descripcion', 'certificado']
        labels = {
            'cargo': 'Cargo desempeñado',
            'empresa': 'Nombre de la empresa', 
            'pais': 'País', 
            'area': 'Area de Trabajo', 
            'fecha_inicio': 'Fecha Inicial',
            'fecha_final': 'Fecha Final',
            'descripcion': 'Actividades Realizadas',
            'certificado': 'Certificado Laboral',
        }
        widgets = { 
            'cargo': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'empresa': forms.TextInput(attrs = {'class': 'form-control'}),
            'pais': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'area': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'fecha_inicio': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control', 'max': fecha_actual}),
            'fecha_final': forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date', 'class': 'form-control', 'max': fecha_actual}),
            'descripcion': forms.Textarea(attrs = {'class': 'form-control'}),
            'certificado':forms.FileInput(attrs = {'class': 'form-control'}),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postulante'] = forms.CharField(widget=forms.HiddenInput())
        self.fields['certificado'].validators.append(validar_pdf)
        self.fields['certificado'].widget.attrs.update({'accept': 'application/pdf'})


class EducacionForm(forms.ModelForm):
    class Meta: 
        nivel = {'':'- Seleccione -','Bachiller':'Bachiller', 'Técnico':'Técnico', 'Universitario':'Universitario', 'Magister':'Magister', 'Doctorado':'Doctorado', 'Otro':'Otro'}
        estado = {'':'- Seleccione -','En Curso':'En Curso', 'Graduado':'Graduado', 'Abandonado':'Abandonado'}
        model = Educacion
        fields = ['titulo_edu','pais_edu','institucion_edu','nivel_edu', 'estado_edu', 'descripcion_edu', 'titulo']
        labels = {
            'titulo_edu': 'Título',
            'pais_edu': 'País', 
            'institucion_edu': 'Institución', 
            'nivel_edu': 'Nivel', 
            'estado_edu': 'Estado',
            'descripcion_edu': 'Descripción',
            'titulo': 'Subir Título',
        }
        widgets = { 
            
            'titulo_edu': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'pais_edu': forms.TextInput(attrs = {'class': 'form-control', 'pattern': '^[A-Za-z\s]+$', 'title': 'Por favor, ingrese solo letras'}),
            'institucion_edu': forms.TextInput(attrs = {'class': 'form-control'}),
            'nivel_edu': forms.Select(choices=nivel.items(),attrs = {'class': 'form-control'}),
            'estado_edu': forms.Select(choices=estado.items(), attrs = {'class': 'form-control'}),
            'descripcion_edu': forms.TextInput(attrs = {'class': 'form-control'}),
            'titulo':forms.FileInput(attrs = {'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_educacion_fk'] = forms.CharField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super().clean()
        estado_edu = cleaned_data.get('estado_edu')
        titulo = cleaned_data.get('titulo')
        
        # Verificar si el estado es "Graduado" y el campo "titulo" está vacío
        if estado_edu == 'Graduado' and not titulo:
            self.add_error('titulo', 'Si se encuentra graduado, debe subir su título para respaldar la información')

        return cleaned_data



class EntrevistaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EntrevistaForm, self).__init__(*args, **kwargs)
        # Establecer la hora predeterminada como 12:00 PM
        self.fields['hora'].initial = '12:00'
        
    class Meta:
        model = Entrevista
        fields = ['fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
           'hora': forms.TextInput(attrs={'type': 'time', 'class': 'form-control', 'placeholder': 'HH:MM'}),
        }