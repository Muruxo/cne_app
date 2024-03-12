from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from .utils import * 
from .models import *
from  .forms import *
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings

# import tkinter as tk
# from tkinter import messagebox

# root = tk.Tk() 
# root.mainloop()


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
        messages.error(request, 'Publicación Eliminada')
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

# def postular(request, empleo_id, postulante_id): 
#     publicacion = Empleo.objects.get(pk = publicacion_id)
#     form = EmpleoForm(request.POST or None, instance = publicacion)
#     if request.POST: 
#         form = EmpleoForm(request.POST)
#         if form.is_valid():
#             form.save()
#         messages.success(request, 'Postulación Exitosa')
#         return redirect()  
    
def descripcion(request, empleo_id): 

    empleo = Empleo.objects.get(pk = empleo_id)
    contenido = {
        'empleo' : empleo
    }
    template = "descripcion.html"
    return render(request, template, contenido)


#FORM DATOS PERSONALES POSTULANTE

@login_required   
def agregarDatosPersonales(request, id): 
    usuario = User.objects.get(pk = id )
    contenido = {}
    if request.method == 'POST':  
        form = DatosPersonalesForm(request.POST,  request.FILES)
        if form.is_valid():
            postulante = form.save(commit=False)
            postulante.usuario_postulante = usuario  # Asigna el nombre de usuario al campo correspondiente
            postulante.save()
            messages.success(request, 'Informacion agregada con éxito')
        return redirect(agregarDatosAdicionales, id) 

    else:
        form = DatosPersonalesForm(initial={'usuario_postulante': id})  # Establece el valor inicial del campo de nombre de usuario
        contenido['form'] = form
        contenido['usuario_postulante'] = usuario
    return render(request, 'DatosPersonales.html', contenido)

@login_required   
def profile(request): 
    usuario = request.user
    if request.POST: 
        form = DatosPersonalesForm(request.POST)
        if form.is_valid():
            postulante = form.save(commit=False)
            postulante.usuario_postulante = usuario  # Asigna el nombre de usuario al campo correspondiente
            postulante.save()
        messages.success(request, 'Información Añadida')
        return redirect(index)
    return render(request, 'profile.html', {'form':DatosPersonalesForm})
    
# def profile(request): 
#     usuario = request.user.pk
#     contenido = {}
#     if request.method == 'POST':  
#         form = DatosPersonalesForm(request.POST,  request.FILES)
#         if form.is_valid():
#             postulante = form.save(commit=False)
#             postulante.usuario_postulante.pk = usuario  # Asigna el nombre de usuario al campo correspondiente
#             postulante.save()
#             messages.success(request, 'Informacion agregada con éxito')
#         return redirect(index, usuario) 

#     else:
#         form = DatosPersonalesForm(initial={'usuario_postulante': usuario})  # Establece el valor inicial del campo de nombre de usuario
#         contenido['form'] = form
#         contenido['usuario_postulante'] = usuario
#     return render(request, 'profile.html', contenido)

# @login_required   
# def subirCurriculum(request, id): 
#     if request.method == 'POST':  
#         form = CurriculumForm(request.POST, request.FILES)
#         if form.is_valid():
#             curriculum = form.save(commit=False)
#             curriculum.id = request.usuario_postulante.id
#             messages.success(request, 'Informacion agregada con éxito')
#         return redirect(index, id)  
#     return render(request, 'subirCurriculum.html', form)




@login_required   
def subirCurriculum(request): 
    id = request.user
    postulante = get_object_or_404(Postulante, usuario_postulante =id)
    if request.method == 'POST':  
        form = CurriculumForm(request.POST, request.FILES, instance=postulante)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Información actualizada con éxito!')
            return redirect(index)
    else:
        form = CurriculumForm(instance=postulante)
    
    return render(request, 'subirCurriculum.html', {'form': form, 'postulante': postulante})


@login_required
def agregarDatosAdicionales(request, id):
    usuario = Postulante.objects.get(pk = id)
    contenido = {}
    if request.method == 'POST': 
        form = ExperienciaForm(request.POST, request.FILES)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.postulante = usuario  # Asigna el nombre de usuario al campo correspondiente
            experiencia.save()
            messages.success(request, 'Informacion agregada con éxito')
            return redirect(experiencias, id)
    else:
        form = ExperienciaForm(initial={'postulante': id})  # Establece el valor inicial del campo de nombre de usuario
        contenido['form'] = form
        contenido['postulante'] = usuario
    return render(request, 'DatosAd.html', contenido)


#  AGREGAR EDUCACION NUEVO

@login_required
def agregarDatosEducacion(request, id):
    usuario = Postulante.objects.get(pk = id)
    contenido = {}
    if request.method == 'POST': 
        form = EducacionForm(request.POST, request.FILES)
        if form.is_valid():
            educacion = form.save(commit=False)
            educacion.id_educacion_fk = usuario  # Asigna el nombre de usuario al campo correspondiente
            educacion.save()
            messages.success(request, 'Informacion agregada con éxito')
            return redirect(educaciones, id=usuario)
    else:
        form = EducacionForm(initial={'id_educacion_fk': id})  # Establece el valor inicial del campo de nombre de usuario
        contenido['form'] = form
        contenido['id_educacion_fk'] = id
    return render(request, 'DatosEducacion.html', contenido)

@login_required
def actualizarDatosPersonales(request): 
        id = request.user
        postulante = Postulante.objects.get(usuario_postulante = id)
        form = DatosPersonalesForm(request.POST or None, instance = postulante)
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Publicación Actualizada')
            return redirect(index)  
        return render(request, 'actualizarDatosPersonales.html', {'postulante':postulante, 'form': form})

@login_required
def actualizarEducaciones(request, id): 
        educacion = get_object_or_404(Educacion, pk=id)
        postulante_id = educacion.id_educacion_fk.pk
        form = EducacionForm(request.POST or None, instance = educacion)
        if request.method == 'POST':
            if form.is_valid(): 
                form.save() 
                messages.success(request, 'Publicación Actualizada')
                return redirect(educaciones, id=postulante_id)  
        return render(request, 'actualizarEducacion.html', {'id_educacion_fk':educacion, 'form': form})

@login_required
def actualizarExperiencias(request, id): 
        experiencia = Experiencia.objects.get(pk = id)
        form = ExperienciaForm(request.POST or None, instance = experiencia)
        postulante_id = experiencia.postulante.pk
        if form.is_valid(): 
            form.save()
            messages.success(request, 'Publicación Actualizada')
            return redirect(experiencias, id=postulante_id)  
        return render(request, 'actualizarExperiencia.html', {'postulante':experiencia, 'form': form})

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


# NUEVA FUNCION AGREGAR DATOS (ARREGLAR PROBLEMA FOREIGNKEY)
# def agregarDatosEducacion(request, username): 
#     usuario = User.objects.get(username = username)
#     contenido = {}
#     if request.method == 'POST':  
#         form = EducacionForm(request.POST)
#         if form.is_valid():
#             educacion = form.save(commit=False)
#             educacion.id_educacion_fk = usuario
#             educacion.save()
#             messages.success(request, 'Informacion agregada con éxito')
#             return redirect(index, username)  
    
#     else:
#         form = EducacionForm(initial={'id_educacion_fk': username})  # Establece el valor inicial del campo de nombre de usuario
#         contenido['form'] = form
#         contenido['id_educacion_fk'] = usuario

#   



# AGREGAR EDUCACION ANTIGUO

# def agregarDatosEducacion(request, id): 
#      usuario = User.objects.get(pk = id )
#      form = EducacionForm(request.POST or None , instance = usuario)
#      if request.POST: 
#         if form.is_valid():
#             form.save()
#         messages.success(request, 'Informacion agregada con éxito')
#         return redirect(index)  

#      return render(request, 'DatosEducacion.html', {'id_educacion_fk': usuario, 'form':form})


@login_required
def experiencias(request):
    id = request.user
    usuario = Postulante.objects.get(usuario_postulante = id)
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


@login_required
def educaciones(request):
    id = request.user
    usuario = Postulante.objects.get(usuario_postulante = id)
    educacion = Educacion.objects.filter(id_educacion_fk = usuario)
    return render(request, 'verEducacion.html', {'educacion': educacion})


# def lista_postulantes(request, lista_id):
#     publicacion = User.objects.get(pk = lista_id)
#     contenido = {
#         'postulados' : publicacion
#     }
#     template = "lista_postulantes.html"
#     return render(request, template, contenido)
@login_required
def lista_postulantes(request):
    c={}
    c['postulantes'] = User.objects.all()
    return render(request, 'lista_postulantes.html', c)

# @login_required
# def descripcion(request, empleo_id): 
#     empleo = Empleo.objects.get(pk = empleo_id)
#     contenido = {
#         'empleo' : empleo
#     }
#     template = "descripcion.html"
#     return render(request, template, contenido)

@login_required
def guardar_postulacion(request, empleo_nombre):
        
        nombre_usuario = request.user

        if request.method == 'POST':
            # Obtener los datos enviados en la solicitud POST
            usuario = User.objects.get(username=nombre_usuario)
            postulante = Postulante.objects.get(usuario_postulante=usuario)
            resultado_experiencia = Experiencia.objects.filter(postulante=postulante).exists()
            resultado_educacion = Educacion.objects.filter(id_educacion_fk=postulante).exists()

            if resultado_experiencia and resultado_educacion: 
                
                usuario = request.user
                postulante = Postulante.objects.get(usuario_postulante=usuario)
                trabajo = Empleo.objects.get(nombre_empleo=empleo_nombre)

                if Postulados.objects.filter(id_postulados_fk=postulante, id_empleo_fk=trabajo).exists():
                    messages.error(request, 'Ya te encuentras postulado para esta vacante')
                    return redirect(index)
            
                # Aquí puedes guardar los datos en el modelo que desees
                # Por ejemplo, puedes guardarlos en el modelo Postulados
                # standard = trabajo.anos_minimos_experiencia
                
                exp_usuario = Experiencia.objects.filter(postulante=postulante)

                               
                experiencia_total = exp_usuario.count()

                # for  experiencia in resultado_experiencia:
                #     if experiencia:
                #         experiencia_total += 1
                        
                educacion_total = 0
                educaciones = Educacion.objects.filter(id_educacion_fk=postulante)
                
                for educacion in educaciones:
                    if educacion.nivel_edu == 'Bachiller' and educacion.estado_edu == 'Graduado':
                        educacion_total += 1
                    elif educacion.nivel_edu == 'Técnico' and educacion.estado_edu == 'Graduado':
                        educacion_total += 2
                    elif educacion.nivel_edu == 'Universitario' and educacion.estado_edu == 'Graduado':
                        educacion_total += 3
                    elif educacion.nivel_edu == 'Magister' and educacion.estado_edu == 'Graduado':
                        educacion_total += 4
                    elif educacion.nivel_edu == 'Doctorado' and educacion.estado_edu == 'Graduado':
                        educacion_total += 5
                    else: 
                        educacion_total += 1 
                        
                calficacion_total = experiencia_total + educacion_total
                
                # Ejemplo de cómo podrías guardar los datos en el modelo Postulados
                postulacion = Postulados.objects.create(
                    estado_postulado='Activo',  # Puedes establecer un estado por defecto
                    id_postulados_fk=postulante,
                    id_empleo_fk=trabajo,
                    calificacion = calficacion_total
                )

                # Redirigir al usuario a otra página
                messages.success(request, 'Postulacion exitosa')
                return redirect(index)  # Ajusta esto según sea necesario
            else: 
                messages.error(request, 'Debe completar sus datos de Experiencia y Educación')
                return redirect(index)

        
        else:
            # Si es una solicitud GET, simplemente muestra los datos del empleo
            empleo = Empleo.objects.get(nombre_empleo = empleo_nombre)
        contenido = {
            'empleo' : empleo
        }
        template = "descripcion.html"
        return render(request, template, contenido)
    





@login_required
def congrats(request, id_postulados_fk):
    c={}
    c['congrats'] = Postulados.objects.get(pk = id_postulados_fk)
    return render(request, 'congrats.html', c)

@login_required
def extraer_id_postulante(request): 
    id = Postulante.objects.all()
    return render(request, 'usersidebar.html', {'postulantes': id})

@login_required
def postulante_por_empleo(request, empleo): 
    datosempleo = Empleo.objects.get(pk=empleo)        
    c={}
    c['postulados'] = Postulados.objects.filter(id_empleo_fk = empleo)
    c['empleo'] = datosempleo

    return render(request, 'postulanteporempleo.html', c)


@login_required
def descripcionpostulante(request, id): 
    experienciapostulante = Experiencia.objects.filter(postulante = id)
    educacionpostulante = Educacion.objects.filter(id_educacion_fk = id)
    
    c={}
    c['persona'] = Postulante.objects.get(id = id)
    c['experiencia'] = experienciapostulante
    c['educacion'] = educacionpostulante
    
    
    return render (request, 'descripcionpostulante.html', c) 





def redireccionPostular(request, id):
    # Realiza la consulta a la base de datos
    resultado_consulta = Postulante.objects.filter(id = id).exists()

    # Si el resultado de la consulta cumple tu condición
    if resultado_consulta:
        return actualizarDatosPersonales(request, id)  # Redirige a la primera función de vista
    else:
        return agregarDatosPersonales(request, id)  # Redirige a la segunda función de vista


def activarempleo(request, id):
    
    empleo = Empleo.objects.get(pk = id)
    empleo.estado = 1 if empleo.estado == 0 else 0 
    # respuesta = messagebox.askokcancel(message="¿Está seguro de Activar este Empleo?", title="Confirmación")
    # if respuesta: 
    empleo.save() 
    messages.success(request, 'Empleo Activado')
    return redirect('home')
    # else: 
    #     return redirect('home')
    
def desactivarempleo(request, id):
    
    empleo = Empleo.objects.get(pk = id)
    empleo.estado = 0 if empleo.estado == 1 else 1
    messages.success(request, 'Empleo Desactivado')
    empleo.save() 
    return redirect('home')

def UsuarioPostulaciones(request):
    nombre_usuario = request.user
    usuario = Postulante.objects.get(usuario_postulante = nombre_usuario)

    c={}
    c['postulados'] = Postulados.objects.filter(id_postulados_fk = usuario)
    empleo = c['postulados'].first().id_empleo_fk
    c['empleo'] = Empleo.objects.get(nombre_empleo = empleo)
    empleo_nombre = c['empleo']

    return render(request, 'postulaciones.html',{'c': c, 'empleo_nombre': empleo_nombre, 'nombre_usuario': nombre_usuario})

def entrevista(request, postulante_id, empleo_id): 
    
    postulante = Postulante.objects.get(pk=postulante_id)
    empleo = Empleo.objects.get(pk=empleo_id)
    estado = Postulados.objects.get(id_postulados_fk = postulante_id, id_empleo_fk = empleo_id)
    if request.method == 'POST':
        form = EntrevistaForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario
            # Por ejemplo, guardar la entrevista en la base de datos
            entrevista = form.save(commit=False)
            entrevista.postulante = postulante
            entrevista.empleo = empleo
            estado.estado_postulado =  "Entrevista"
            estado.save() 
            form.save()
            
             # Enviar correo electrónico
            asunto = 'Nueva entrevista programada'
            mensaje = f'Se ha programado una nueva entrevista para {postulante.nombre} para el empleo {empleo.nombre_empleo} el {entrevista.fecha} a las {entrevista.hora}.'
            destinatarios = [settings.EMAIL_HOST_USER, postulante.email]  # Poner aquí la dirección de correo a la que quieres enviar el mensaje

            send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, destinatarios, fail_silently=False)

            return redirect('postulanteporempleo', empleo_id)
            # return HttpResponse('Entrevista creada correctamente.')
    else:
        form = EntrevistaForm()
    return render(request, 'entrevista.html', {'form': form})