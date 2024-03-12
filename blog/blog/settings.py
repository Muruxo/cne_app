"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.contrib.messages import constants as messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xf1aivoj9!in*&uw85j)pyajl1sorg40f0=ox_fot-)s%e$0s8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'Muruxo.pythonanywhere.com',
    '127.0.0.1'
]

# Redireccionar al iniciar y salir de sesión 

# LOGIN_REDIRECT_URL = 'home',
# LOGOUT_REDIRECT_URL ='index'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django_extensions',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'app',
    'e_mail',
    'components',
    'extra_pages',
    'email_templates',
    'layouts',
    'authentication',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.sites',
    'widget_tweaks',
    'imagekit',
    'rest_framework',
    'email_servie'
]

MIDDLEWARE = [
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates',
                 '/home/Muruxo/cne_app/blog/templates',
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Muruxo$db',
#         'USER': 'Muruxo',
#         'PASSWORD': 'Liceo2024',
#         'HOST': 'Muruxo.mysql.pythonanywhere-services.com',
#         'PORT': '3306'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
 
 
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"),
    #os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "apps/templates/static"),
    os.path.join(BASE_DIR, 'blog'),
]
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
 
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--port', '8888',
]
IPYTHON_KERNEL_DISPLAY_NAME = 'Django Kernel'

# All Auth Config 
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

# Otras configuraciones de allauth (opcional)
# Puedes personalizar el comportamiento con las siguientes opciones:
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR,'assets')




#Email settings
DEFAULT_FROM_EMAIL = 'info.vacantes3@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'gvos ebkv kdcg veai'


#  All Auth Configurations
# LOGIN_REDIRECT_URL = "/"
# LOGIN_URL = "account_login"
# ACCOUNT_LOGOUT_ON_GET = False
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True

# social Additional configuration settings
SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_UNIQUE_EMAIL = True
SOCIALACCOUNT_LOGIN_ON_GET = True

#  All auth form customaization
ACCOUNT_FORMS = {
    "login": "blog.forms.UserLoginForm",
    "signup": "blog.forms.UserRegistrationForm",
    "change_password": "blog.forms.PasswordChangeForm",
    "set_password": "blog.forms.PasswordSetForm",
    "reset_password": "blog.forms.PasswordResetForm",
    "reset_password_from_key": "blog.forms.PasswordResetKeyForm",
    "profile": "app.forms.DatosPersonalesForm",
    
}
# SMTP Configure
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_HOST = "smtp.mailtrap.io"
# EMAIL_PORT = 2525
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "1f37cfc80405c5"
# EMAIL_HOST_PASSWORD = "5f7e38f28ae814"
# DEFAULT_FROM_EMAIL = "1f37cfc80405c5"

CRISPY_TEMPLATE_PACK = 'bootstrap5'

SITE_ID = 1

# Provider Configurations
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': 
        {
            'client_id': '556542475411-atai04oepna72lf526enbkq3b5d6sod1.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    }
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# client id = '556542475411-atai04oepna72lf526enbkq3b5d6sod1.apps.googleusercontent.com'
# client secret = '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'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
