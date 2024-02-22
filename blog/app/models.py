from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo      = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=250)
    email       = models.EmailField(blank=True, null=True)
    
    def __str__(self): 
        return self.titulo
    class Meta: 
        verbose_name_plural = 'Publicaciones'

class Postulante(models.Model):
    user = models.OneToOneField(User, related_name='perfil', on_delete=models.CASCADE, null=True)
    nombre_postulante = models.CharField(max_length=144)
    apellido_postulante = models.CharField(max_length=144,blank=False,null=False)
    genero_postulante = models.CharField(max_length=144,blank=False,null=False)
    edad_postulante = models.IntegerField(blank=False,null=False, validators=[MaxValueValidator(99)])
    direccion_postulante = models.CharField(max_length=200,blank=False,null=False)
    email_postulante = models.EmailField(max_length=150,blank=False,null=False)
    telefono_postulante = models.IntegerField(blank=False,null=False, validators=[MaxValueValidator(9999999999)])
    ciudad_postulante = models.CharField(max_length=144,blank=False, null=False)
    # Falta numero de cedula, nacionalidad
    
    def __str__(self) -> str:
            return f'{self.pk} - {self.nombre_postulante}'

class Detallepostulante(models.Model):
    descripcion_laboral = models.TextField(blank=True,null=True)
    idioma_laboral = models.CharField(max_length=255,blank=True,null=True)
    id_postulante_fk = models.ForeignKey(Postulante, related_name='postulante', on_delete=models.CASCADE,null=True)

    def __str__(self)->str:
        return f'{self.experiencia_laboral}'

class Experiencia(models.Model): 
    id_experiencia_fk = models.ForeignKey(Postulante, related_name='postulanteexp', on_delete=models.CASCADE,null=True)
    cargo_exp = models.CharField(max_length=255,blank=False,null=False)
    empresa_exp = models.CharField(max_length=255,blank=False,null=False)
    pais_exp = models.CharField(max_length=255,blank=False,null=False)
    area_exo = models.CharField(max_length=255,blank=False,null=False)
    finicio_exp = models.DateField(blank=False, null= False)
    ffinal_exp = models.DateField(blank=True, null=True)
    descripcion_exp = models.TextField(blank=True,null=True)
    
    def __str__(self)->str:
        return f'{self.empresa_exp}'
    class Meta: 
        verbose_name_plural = 'Experiencia'
        
        
class Niveltitulo(models.Model): 
    nivel = models.CharField(max_length=144,blank=False, null=False)
    
    def __str__(self)-> str:
        return f'{self.nivel}'

    class Meta: 
        verbose_name_plural = 'Niveltitulo'
        
    
class Educacion(models.Model): 
    id_educacion_fk = models.ForeignKey(Postulante, related_name='postulanteedu', on_delete=models.CASCADE,null=True)
    titulo_edu = models.CharField(max_length=255,blank=False,null=False)
    pais_edu = models.CharField(max_length=255,blank=False,null=False)
    institucion_edu = models.CharField(max_length=255,blank=False,null=False)
    nivel_edu= models.ForeignKey(Niveltitulo, related_name='nivelid', on_delete=models.CASCADE,null=True)
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
    
    def __str__(self)->str:
        return f'{self.nombre_empleo}'


class Postulados(models.Model):
    estado_postulado = models.CharField(max_length=144,blank=False, null=False)
    fecha_postulado = models.DateField(default=timezone.now, blank=False,null=False)
    id_postulados_fk = models.ForeignKey(Postulante, related_name='postulado', on_delete=models.SET_NULL,null=True)
    id_empleo_fk = models.ForeignKey(Empleo, related_name='postulados', on_delete=models.SET_NULL,null=True)

    def __str__(self)-> str:
        return f'{self.estado_postulado}'

    class Meta: 
        verbose_name_plural = 'Postulados'


