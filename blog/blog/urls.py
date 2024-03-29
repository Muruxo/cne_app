"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from app.views import *
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView, DashboardView
from django.conf import settings
from django.conf.urls.static import static
from email_servie.api.views import EmailAPIView


urlpatterns = [
    
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('', index, name='index'),
    path('index', index, name='index'),
    path('home', home, name='home'),
    path('prueba/<id>',prueba, name='prueba'),
    path('lista_postulantes', lista_postulantes, name='lista_postulantes'),
    path('agregar', agregar, name = 'agregar'),
    path('eliminar/<publicacion_id>', eliminar, name = 'eliminar'),
    path('actualizar/<publicacion_id>', actualizar, name ="actualizar"), 
    # path('postular', postular, name = 'postular'),
    path('descripcion/<empleo_nombre>', guardar_postulacion , name ="guardar_postulacion"), 
    path('accounts/', include('allauth.urls')),
    path('DatosPer/', actualizarDatosPersonales, name='DatosPer'),
    path('subirCurriculum/', subirCurriculum, name='subirCurriculum'),
    path('DatosAd/', agregarDatosAdicionales, name='DatosAd'),
    path('DatosEdu/', agregarDatosEducacion, name='DatosEdu'),
    path('actualizarDatosPersonales/<str:id>', actualizarDatosPersonales, name ="actualizarDatosPersonales"), 
    path('actualizarExperiencia/<str:id>', actualizarExperiencias, name ="actualizarExperiencia"), 
    path('actualizarEducacion/<str:id>', actualizarEducaciones, name ="actualizarEducacion"), 
    path('verExperiencias/', experiencias, name='Experiencias'),
    path('verEducaciones/', educaciones, name='Educaciones'),
    path('postulaciones/', UsuarioPostulaciones, name='postulaciones'),
    path('activar/<id>', activarempleo, name='activar'),
    path('desactivar/<int:id>', desactivarempleo, name='desactivar'),
    path('congrats/<lista_id>', congrats, name= 'congrats'),
    path('postulanteporempleo/<empleo>', postulante_por_empleo, name= 'postulanteporempleo'),
    path('descripcionpostulante/<str:id>/<empleo_id>', descripcionpostulante, name= 'descripcionpostulante'),
    path('admin/', admin.site.urls),
    path('send-email', EmailAPIView.as_view(), name='send-email'),
    path('accounts/profile/', profile, name='profile'),
    path('entrevista/<postulante_id>/<empleo_id>', entrevista, name='entrevista'),
    path('contratar/<postulante_id>/<empleo_id>', contratar, name='contratar'),
    path('rechazar/<postulante_id>/<empleo_id>', rechazar, name='rechazar'),
   
   
    # Email
    path("email/", include("e_mail.urls")),
    # Components
    path("components/", include("components.urls")),
    # Extra_Pages
    path("extra_pages/", include("extra_pages.urls")),
    # Extra_Pages
    path("email_templates/", include("email_templates.urls")),
    # layouts
    path("layouts/", include("layouts.urls")),
    path("authentication/", include("authentication.urls")),

    path(
        "account/password/change/",
        login_required(MyPasswordChangeView.as_view()),name="account_change_password",),
    path(
        "account/password/set/",
        login_required(MyPasswordSetView.as_view()),name="account_set_password",),

    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

