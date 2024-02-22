from django import forms
from django.forms import ModelForm

from .models import Publicacion

class PublicacionForm(ModelForm):
    class Meta: 
        model = Publicacion
        fields = '__all__'
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'genero': 'Genero', 
            'edad': 'Edad',
            'email': 'Email',
            'telefono': 'Telefono',
            'ciudad': 'Ciudad', 
            
            
        }
        widgets = {
            'nombre': forms.TextInput(attrs = {'class': 'form-control'}),
            'apellido': forms.TextInput(attrs = {'class': 'form-control'}),
            'genero': forms.TextInput(attrs = {'class': 'form-control'}),
            'edad': forms.TextInput(attrs = {'class': 'form-control'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs = {'class': 'form-control'}),
        }