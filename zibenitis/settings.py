"""
Django settings for zibenitis project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/

"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECRET_KEY is stored in Environmental variable. Otherwise default value (fake key, not used in production)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

DEVELOPMENT = bool(os.environ.get('DJANGO_DEBUG', True))

# Settings for production
if not DEVELOPMENT:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_SSL_REDIRECT = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    ALLOWED_HOSTS = ['zibenitis.se', 'www.zibenitis.se', 'dev.zibenitis.se']
else:
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    SECURE_SSL_REDIRECT = False
    SECURE_BROWSER_XSS_FILTER = False
    SECURE_CONTENT_TYPE_NOSNIFF = False
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
            ],
            'debug': DEBUG,
        }
    }
]

# Enable tables and other non-core features
MARKDOWN_EXTENSIONS = ['extra']

SITE_ID = 1

# Application definition
INSTALLED_APPS = (
    'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'markdownx',
    'photologue',
    'sortedm2m',  # with photologue

    'zibenitis.apps.dancers',
    'zibenitis.apps.blog',
    'zibenitis.apps.events',
    'zibenitis.apps.utils',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'zibenitis.urls'

WSGI_APPLICATION = 'zibenitis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'zibenitis/../db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'lv'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static-loc'), ]  # possible to add multiple paths to directories
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Adding definition of media (file) storage directroy
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Added change from the web repository
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
