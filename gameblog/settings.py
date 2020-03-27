"""
Django settings for gameblog project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

import dj_database_url



#from django.urls import reverse_lazy

#ABSOLUTE_URL_OVVERRIDES={
#    'auth.user':lambda u:reverse_lazy('home_user', args=[u.id])
#}

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nt6b6nshi+u$#i+ofb&n6enk1a#z(7n3%atz$qfnev(oz=cdld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'social_django',
    #приложения для создания карты сайта
    'django.contrib.sites', #(как и в примере из инета, почему то комментирование этой строчки решило проблему DoesNotExist at /sitemap.xml/)
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    #'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gameblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #процессоры для авторизации через вконтакте
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'gameblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'gameblog',
        'USER':'postgres',
        'PASSWORD':'Python777',
        'HOST':'127.0.0.1',
        'PORT':'5432',
    }
}


db_from_env=dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR, '/static/'),]
STATIC_ROOT=os.path.join(BASE_DIR, 'static/')


MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media/')


EMAIL_HOST='smtp.gmail.com';
EMAIL_PORT=587;
EMAIL_HOST_USER='imperecdiego@gmail.com';
EMAIL_HOST_PASSWORD='Python777';
EMAIL_USE_TLS=True;
EMAIL_USE_SSL=False;


LOGIN_REDIRECT_URL='posts_list_url'
LOGIN_URL='login'
LOGOUT_URL='logout'


#Этот параметр разрешает использовать для хранения данных поле типа JSONB, поддерживаемое Postgress
SOCIAL_AUTH_POSTGRES_JSONFIELD=True


AUTHENTICATION_BACKENDS=(

    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',

    )

#Секретные ключи из Фейсбука для подключения
SOCIAL_AUTH_FACEBOOK_KEY='504751600196436'
SOCIAL_AUTH_FACEBOOK_SECRET='8436201b3f079d38fc66c92adb858294'


#Секретные ключи из Гугла для подключения
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='597719370099-6ia2o0bahvk2ojfbd48244fv6u9kpms1.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='o3r789lWCa4GjDGbTq8V5bbd'



##Секретные ключи из Вконтакте для подключения
SOCIAL_AUTH_VK_OAUTH2_KEY='7371500'
SOCIAL_AUTH_VK_OAUTH2_SECRET='l59yMCIEjIUH2Vb0jfh7'