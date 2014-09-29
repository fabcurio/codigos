
import os
from unipath import Path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

RUTA_PROYECTO=Path(__file__).ancestor(2)


SECRET_KEY = 'tgp9q9=cqz&&i5^@u^87e5&_$tier+gup+d#o_x#kse8e+$oa!'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = (

    RUTA_PROYECTO.child('templates'),

)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.noticias',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'fadgames.urls'

WSGI_APPLICATION = 'fadgames.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'fadgames.sqlite3'),
    }
}



LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = RUTA_PROYECTO.child('media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'


