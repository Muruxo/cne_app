from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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


def agregarDatosAdicionales(request): 
    if request.POST: 
        ExperienciaForm1 = ExperienciaForm(request.POST)
        
        if ExperienciaForm1.is_valid(): 
            ExperienciaForm1.save()
        messages.success(request, 'Informacion agregada con éxito')
        return redirect(agregarDatosEducacion)  

    return render(request, 'DatosAd.html', {'form1':ExperienciaForm}) #'form2': DatosAdicionalesForm

  
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
