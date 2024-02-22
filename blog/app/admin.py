from django.contrib import admin

from .models import Publicacion, Postulante, Detallepostulante, Ciudad, Empleo, Postulados, Experiencia, Educacion, Niveltitulo


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'email')


@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'nombre_postulante',
        'apellido_postulante',
        'genero_postulante',
        'edad_postulante',
        'direccion_postulante',
        'email_postulante',
        'telefono_postulante',
        'ciudad_postulante',
    )
    list_filter = ('user',)


@admin.register(Detallepostulante)
class DetallepostulanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'descripcion_laboral',
        'idioma_laboral',
        'id_postulante_fk',
    )
    list_filter = ('id_postulante_fk',)


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_ciudad', 'telefono_ciudad', 'email_ciudad')


@admin.register(Empleo)
class EmpleoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre_empleo',
        'descripcion_empleo',
        'fecha_empleo',
        'area_empleo',
        'modalidad_empleo',
        'tiempo_empleo',
        'id_ciudad_fk',
    )
    list_filter = ('fecha_empleo', 'id_ciudad_fk')


@admin.register(Postulados)
class PostuladosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estado_postulado',
        'fecha_postulado',
        'id_postulados_fk',
        'id_empleo_fk',
    )
    list_filter = ('fecha_postulado', 'id_postulados_fk', 'id_empleo_fk')

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cargo_exp',
        'empresa_exp',
        'pais_exp',
        'area_exo',
        'finicio_exp',
        'ffinal_exp',
        'descripcion_exp',
    )
    list_filter = ('finicio_exp', 'ffinal_exp')


@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo_edu',
        'pais_edu',
        'institucion_edu',
        'nivel_edu',
        'estado_edu',
        'descripcion_edu',
    )

@admin.register(Niveltitulo)
class NiveltituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel')
