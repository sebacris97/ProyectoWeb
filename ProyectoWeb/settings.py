"""
Django settings for ProyectoWeb project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# Don't forget to import os at the beginning of the file
import os

from django.contrib.messages import constants as error_messages
from pathlib import Path

# Import dj-database-url at the beginning of the file.
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'django-insecure-p1)9plyziq(%$fsmwcq@)cv*%mwlc@+h^z7kknajepw+(5p9)x'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]").split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ProyectoWebApp',
    'servicios',
    'blog',
    'contacto',
    'tienda',
    'carro',
    'autenticacion',
    'pedidos',
    
    'rangefilter', 
    'django_cleanup.apps.CleanupConfig',
    'django_admin_listfilter_dropdown',
    'crispy_forms',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    #whitenoise goes after security
       
]

ROOT_URLCONF = 'ProyectoWeb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                'carro.context_processor.importe_total_carro', #cree variable global
            ],
        },
    },
]

WSGI_APPLICATION = 'ProyectoWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ProyectoWeb',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'DATABASE_PORT': '5432',
    }
}
"""

# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'koyebdb',
        'USER': 'koyeb-adm',
        'PASSWORD': 'vXVd1fRqblZ9',
        #'PASSWORD': '',
        'HOST': 'ep-noisy-recipe-a4zdcgf6.us-east-1.pg.koyeb.app',
        'OPTIONS': {'sslmode': 'require'},
    }
}
#DATABASES['PASSWORD'] = os.environ.get('DATABASE_PASSWORD',default = 'your secret database key')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'#'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# This setting informs Django of the URI path from which your static files will be served to users
# Here, they well be accessible at your-domain.onrender.com/static/... or yourcustomdomain.com/static/...

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_HOST = 'smtp.mailersend.net'
EMAIL_HOST_USER = 'MS_T6ibfv@trial-351ndgwyk7rlzqx8.mlsender.net'
EMAIL_HOST_PASSWORD = "TIznJnYJarU99iS9"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


#configurando crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4" 

#para mensajes de error
MESSAGE_TAGS = {
    error_messages.DEBUG: 'debug',
    error_messages.INFO: 'info',
    error_messages.SUCCESS: 'success',
    error_messages.WARNING: 'warning',
    error_messages.ERROR: 'danger',
}


LOGIN_REDIRECT_URL = ''
