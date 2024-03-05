from django.contrib import admin

from .models import Publicacion, Personal, Postulante, Experiencia, Niveltitulo, Educacion, Ciudad, Empleo, Postulados


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'email')


@admin.register(Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nombre', 'apellido')
    list_filter = ('user',)


@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario_postulante',
        'nombre',
        'apellido',
        'genero',
        'edad',
        'direccion',
        'email',
        'telefono',
        'ciudad',
        'curriculum',
    )
    list_filter = ('usuario_postulante',)


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'postulante',
        'cargo',
        'empresa',
        'pais',
        'area',
        'fecha_inicio',
        'fecha_final',
        'descripcion',
    )
    list_filter = ('postulante', 'fecha_inicio', 'fecha_final')


@admin.register(Niveltitulo)
class NiveltituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel')


@admin.register(Educacion)
class EducacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_educacion_fk',
        'titulo_edu',
        'pais_edu',
        'institucion_edu',
        'nivel_edu',
        'estado_edu',
        'descripcion_edu',
    )
    list_filter = ('id_educacion_fk',)


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
        'anos_minimos_experiencia',
        'estado',
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
        'calificacion',
    )
    list_filter = ('fecha_postulado', 'id_postulados_fk', 'id_empleo_fk')