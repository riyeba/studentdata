"""
Django settings for nsu_project project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
# STATIC_URL = 'static/'
BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'
# STATIC_ROOT=os.path.join(BASE_DIR,'static/')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')



STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build','static')

MEDIA_ROOT =  os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'






# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0hd@37u&px3^(@cugjq(uyeuwsigfr+p)u3cqg4v6=k)jn&cof'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['.vercel.app','.now.sh', 'localhost', '127.0.0.1']

# ALLOWED_HOSTS = ['.vercel.app',]
# Application definition

INSTALLED_APPS = [
    'nsuapp',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]
}

ROOT_URLCONF = 'nsu_project.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

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
            ],
        },
    },
]

WSGI_APPLICATION = 'nsu_project.wsgi.application'

# WSGI_APPLICATION = 'nsu_project.wsgi.application'




# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': BASE_DIR / 'db.sqlite3',
#     # }
# }

DATABASES = {
    'default': {
        'ENGINE':"django.db.backends.postgresql_psycopg2",
        'NAME':"test",
        'USER':"postgres",
        'PASSWORD':"3310",
        'HOST':"localhost",
        'PORT':"5432",
    }
}


# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"



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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


