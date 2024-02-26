from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .utils import * 
from .models import *
from  .forms import PublicacionForm, EmpleoForm, DatosPersonalesForm, ExperienciaForm,EducacionForm #DatosAdicionalesForm
from django.http import HttpResponse
def actualizar(request, publicacion_id):
        
        publicacion = Empleo.objects.get(pk = publicacion_id)
        form = EmpleoForm(request.POST or None, instance = publicacion)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Publicación Actualizada')
            return redirect(home)  
        return render(request, 'actualizar.html', {'publicacion':publicacion, 'form': form})
  
      
def eliminar(request, publicacion_id):
  
        publicacion = Empleo.objects.get(pk = publicacion_id)
        publicacion.delete()
        messages.success(request, 'Publicación Eliminada')
        return redirect(home)  

# @login_required    
def agregar(request): 

        if request.POST: 
            form = EmpleoForm(request.POST)
            if form.is_valid():
                form.save()
            messages.success(request, 'Publicacion Añadida')
            return redirect(home)
        return render(request, 'agregar.html', {'form':EmpleoForm})

@login_required
def home(request):
    empleos = Empleo.objects.all()
    return render(request, 'home.html', {'empleos': empleos})

def prueba(request, id):
    c = User.objects.get(pk = id)
    return render(request, 'prueba.html', {'id': c})

def index(request):
    empleos = Empleo.objects.all()
    return render(request, 'index.html', {'empleos': empleos})

def postular(request, empleo_id, postulante_id): 
    # publicacion = Empleo.objects.get(pk = publicacion_id)
    # form = EmpleoForm(request.POST or None, instance = publicacion)
    # if request.POST: 
    #     form = EmpleoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     messages.success(request, 'Postulación Exitosa')
        return redirect()  
    
def descripcion(request, empleo_id): 
    # Query del perro, un perro con el codigo
    empleo = Empleo.objects.get(pk = empleo_id)
    
    # creo un diccionario con el objeto
    contenido = {
        'empleo' : empleo
    }
    template = "descripcion.html"
    return render(request, template, contenido)


#FORM DATOS PERSONALES POSTULANTE

def actualizar(request, publicacion_id): 
        publicacion = Empleo.objects.get(pk = publicacion_id)
        form = EmpleoForm(request.POST or None, instance = publicacion)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Publicación Actualizada')
            return redirect(home)  
        return render(request, 'actualizar.html', {'publicacion':publicacion, 'form': form})
    
def agregarDatosPersonales(request,id): 
    
    idpostulante = User.objects.get(pk = id )
    form = DatosPersonalesForm(request.POST or None, instance = idpostulante)
    if request.POST: 
        if form.is_valid():
            form.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(agregarDatosAdicionales) 

    return render(request, 'DatosPersonales.html', {'datos': idpostulante, 'form':form})

# def agregarDatosAdicionales(request,id): 
    
#     idpostulante = User.objects.get(pk = id )
#     contenido = {}
#     contenido['form'] = ExperienciaForm(request.POST or None, request.FILES or None, instance = idpostulante)
#     if request.POST: 
#         if contenido['form'].is_valid():
#             contenido['form'].save()
#         messages.success(request, 'Informacion agregada con éxito')
#         return redirect(agregarDatosEducacion) 

#     return render(request, 'DatosAd.html', {'datos': idpostulante, 'form':contenido['form']})












# def agregarDatosAdicionales(request, username):
#     usuario = User.objects.get(username = username)
#     contenido = {}
#     if request.method == 'POST': 
#         contenido['form'] = ExperienciaForm(
#                             request.POST or None,
#                             request.FILES or None,
#                             )
#         if contenido['form'].is_valid():
#             contenido['form'].save()
#         messages.success(request, 'Informacion agregada con éxito')
#         return redirect(agregarDatosEducacion)

    
#     return render(request, 'DatosAd.html', {**contenido, 'postulante':usuario})













def agregarDatosAdicionales(request, username):
    usuario = User.objects.get(username = username)
    contenido = {}
    if request.method == 'POST': 
        form = ExperienciaForm(request.POST, request.FILES)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.postulante = usuario  # Asigna el nombre de usuario al campo correspondiente
            experiencia.save()
            messages.success(request, 'Informacion agregada con éxito')
            return redirect(agregarDatosEducacion)
    else:
        form = ExperienciaForm(initial={'postulante': username})  # Establece el valor inicial del campo de nombre de usuario
        contenido['form'] = form
        contenido['postulante'] = usuario
    return render(request, 'DatosAd.html', contenido)


def experiencias(request, username):
    usuario = User.objects.get(username = username)
    experiencia = Experiencia.objects.filter(postulante = usuario)
    return render(request, 'verExperiencias.html', {'experiencia': experiencia})


 #'form2': DatosAdicionalesForm

#------------------------------------------------------------------------------------------------------

# def nuevo_refugio(request):
#     contenido = {}
#     if request.method == 'POST':
#         contenido['form'] = RefugioForm(
#                         request.POST or None,
#                         request.FILES or None,
#                         )
#         if contenido['form'].is_valid():
#             contenido['form'].save()
#             return redirect(contenido['form'].instance.get_absolute_url())
#     contenido['instancia_refugio'] = Refugio()
#     contenido['form'] = RefugioForm(
#         request.POST or None,
#         request.FILES or None,
#         instance = contenido['instancia_refugio']
#     )
#     return render(request, 'formulario_refugio.html', contenido)

  
def agregarDatosEducacion(request): 
    if request.POST: 
        form = EducacionForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(congrats)  

    return render(request, 'DatosEducacion.html', {'form':EducacionForm})


# def lista_postulantes(request, lista_id):
#     publicacion = User.objects.get(pk = lista_id)
#     contenido = {
#         'postulados' : publicacion
#     }
#     template = "lista_postulantes.html"
#     return render(request, template, contenido)

def lista_postulantes(request):
    c={}
    c['postulantes'] = User.objects.all()
    return render(request, 'lista_postulantes.html', c)

def descripcion(request, empleo_id): 
    empleo = Empleo.objects.get(pk = empleo_id)
    contenido = {
        'empleo' : empleo
    }
    template = "descripcion.html"
    return render(request, template, contenido)

def congrats(request, id_postulados_fk):
    c={}
    c['congrats'] = Postulados.objects.get(pk = id_postulados_fk)
    return render(request, 'congrats.html', c)

def extraer_id_postulante(request): 
    id = Postulante.objects.all()
    return render(request, 'usersidebar.html', {'postulantes': id})

def postulante_por_empleo(request, empleo): 
    datosempleo = Empleo.objects.get(pk=empleo)        
    c={}
    c['postulados'] = Postulados.objects.filter(id_empleo_fk = empleo)

    return render(request, 'postulanteporempleo.html', c)

