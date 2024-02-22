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

from app.views import index, home, agregar, eliminar, actualizar, postular, descripcion, agregarDatosAdicionales, agregarDatosEducacion, agregarDatosPersonales
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView, DashboardView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('', DashboardView.as_view(), name='dashboard'),
    
    path('index', index, name='index'),
    path('home', home, name='home'),
    path('agregar', agregar, name = 'agregar'),
    path('eliminar/<publicacion_id>', eliminar, name = 'eliminar'),
    path('actualizar/<publicacion_id>', actualizar, name ="actualizar"), 
    path('postular', postular, name = 'postular'),
    path('descripcion/<empleo_id>', descripcion, name ="descripcion"), 
    path('accounts/', include('allauth.urls')),
    path('DatosPer', agregarDatosPersonales, name='DatosPer'),
    path('DatosAd', agregarDatosAdicionales, name='DatosAd'),
    path('DatosEdu', agregarDatosEducacion, name='DatosEdu'),
    
    path('admin/', admin.site.urls),
    # path('', include('app.urls')),
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
    path('accounts/', include('allauth.urls')),
    
    
]

