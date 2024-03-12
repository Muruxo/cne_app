import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from datetime import date
from django.db import models
from django.urls import reverse

class Publicacion(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    email       = models.EmailField(blank=True, null=True)
    
    def __str__(self): 
        return self.titulo
    class Meta: 
        verbose_name_plural = 'Publicaciones'
        
class Personal(models.Model): 
    user = models.OneToOneField(User, related_name='perfil_admin', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=144,blank=False,null=False)
    apellido = models.CharField(max_length=144,blank=False,null=False) 
    
    def __str__(self): 
        return f'{self.nombre}{self.apellido}'
    class Meta: 
        verbose_name_plural = 'Personal'
    

class Postulante(models.Model):
    usuario_postulante = models.OneToOneField(User, related_name='perfil_postulante', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=144,null=True)
    apellido = models.CharField(max_length=144,blank=False,null=True)
    genero = models.CharField(max_length=144,blank=False,null=True)
    edad = models.IntegerField(blank=False,null=True)
    direccion = models.CharField(max_length=200,blank=False,null=True)
    email = models.EmailField(max_length=150,blank=False,null=True)
    telefono = models.CharField(blank=False,null=True, max_length=10)
    ciudad = models.CharField(max_length=144,blank=False, null=True)
    curriculum = models.FileField(upload_to="media/curriculums", blank=True, null=True)
 
    def __str__(self) -> str:
            return f'{self.usuario_postulante}'
        
        
# Posiblemente puede morir Deprecated
# class Detallepostulante(models.Model):
#     descripcion_laboral = models.TextField(blank=True,null=True)
#     idioma_laboral = models.CharField(max_length=255,blank=True,null=True)
#     id_postulante_fk = models.ForeignKey(User, related_name='postulante', on_delete=models.CASCADE,null=True)

#     def __str__(self)->str:
#         return f'{self.experiencia_laboral}'

class Experiencia(models.Model): 
    postulante = models.ForeignKey(Postulante, related_name='experiencia_postulante', on_delete=models.CASCADE,null=True)
    cargo = models.CharField(max_length=255,blank=False,null=False)
    empresa = models.CharField(max_length=255,blank=False,null=False)
    pais = models.CharField(max_length=255,blank=False,null=False)
    area = models.CharField(max_length=255,blank=False,null=False)
    fecha_inicio = models.DateField(blank=False, null= False)
    fecha_final = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True,null=True)


    
    def tiempo_trabajado(self):
        if self.fecha_final: 
            diferencia = self.fecha_final - self.fecha_inicio
            diferencia = diferencia.days / 365
        else:
            diferencia = date.today() - self.fecha_inicio
            diferencia = diferencia.days / 365
        return round(diferencia, 0)
        
    
    
    def __str__(self)->str:
        return f'{self.empresa}'
    class Meta: 
        verbose_name_plural = 'Experiencia'
        
        
class Niveltitulo(models.Model): 
    nivel = models.CharField(max_length=144,blank=False, null=False)
    
    def __str__(self)-> str:
        return f'{self.nivel}'

    class Meta: 
        verbose_name_plural = 'Niveltitulo'
        
    
class Educacion(models.Model):
    id_educacion_fk = models.ForeignKey(Postulante, related_name='educacion_postulante', on_delete=models.CASCADE,null=True)
    titulo_edu = models.CharField(max_length=255,blank=False,null=False)
    pais_edu = models.CharField(max_length=255,blank=False,null=False)
    institucion_edu = models.CharField(max_length=255,blank=False,null=False)
    nivel_edu= models.CharField(max_length=255,blank=False,null=False)
    estado_edu= models.CharField(max_length=255,blank=False,null=False)
    descripcion_edu = models.TextField(blank=True,null=True)
    
    def __str__(self)->str:
            return f'{self.titulo_edu}'
    class Meta: 
        verbose_name_plural = 'Educacion'
        
class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=144,blank=False, null=False)
    telefono_ciudad = models.IntegerField(blank=False,null=False, validators=[MaxValueValidator(9999999999)])
    email_ciudad = models.EmailField(max_length=150,blank=False,null=False)

    def __str__(self)->str:
        return f'{self.nombre_ciudad}'
    class Meta: 
        verbose_name_plural = 'Ciudades'


class Empleo(models.Model):
    nombre_empleo = models.CharField(max_length=144,blank=False, null=False)
    descripcion_empleo = models.TextField(blank=True,null=True)
    fecha_empleo = models.DateField(default=timezone.now, blank=False,null=False)
    area_empleo = models.CharField(max_length=200,blank=False,null=False)
    modalidad_empleo = models.CharField(max_length=200,blank=False,null=False)
    tiempo_empleo = models.IntegerField(blank=False,null=False, validators=[MaxValueValidator(9999999999)])
    id_ciudad_fk = models.ForeignKey(Ciudad, related_name='ciudad', on_delete=models.SET_NULL,null=True)
    anos_minimos_experiencia = models.IntegerField(blank=True,null=True)
    estado = models.IntegerField(blank=True, null=True)
    
    def __str__(self)->str:
        return f'{self.nombre_empleo}'


class Postulados(models.Model):
    estado_postulado = models.CharField(max_length=144,blank=False, null=False)
    fecha_postulado = models.DateField(default=timezone.now, blank=False,null=False)
    id_postulados_fk = models.ForeignKey(Postulante, related_name='postulado', on_delete=models.SET_NULL,null=True)
    id_empleo_fk = models.ForeignKey(Empleo, related_name='postulados', on_delete=models.SET_NULL,null=True)
    calificacion = models.IntegerField(blank=True, null=True)

    def __str__(self)-> str:
        return f'{self.estado_postulado}'

    class Meta: 
        verbose_name_plural = 'Postulados'


class Entrevista(models.Model):
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    postulante = models.ForeignKey(Postulante, related_name='entrevistapostulante', on_delete=models.SET_NULL,null=True)
    empleo = models.ForeignKey(Empleo, related_name='entrevistaempleo', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"Entrevista para {self.empleo.nombre} el {self.fecha} a las {self.hora}"