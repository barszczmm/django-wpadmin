
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# add apps to path
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
# add wpadmin to path
sys.path.insert(0, os.path.join(BASE_DIR, '..'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&478os2g_tt5g!e+wqgs5h8#-u8ydqhkohnc6u&*yxg9cu@rm5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    # Django WP Admin must be before django.contrib.admin
    'wpadmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authors',
    'books',
    'cds',
    'dvds',
    'test_app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'test_project.urls'

WSGI_APPLICATION = 'test_project.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'files/static-collected/')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WPADMIN = {
    'adminpanel': {
        'admin_site': 'test_project.admin.admin',
        'title': 'Django admin panel',
        'menu': {
            'top': 'wpadmin.menu.menus.BasicTopMenu',
            'left': 'wpadmin.menu.menus.BasicLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': True,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/sunrise.css',
    },
    'userpanel': {
        'admin_site': 'test_project.admin.user',
        'title': 'Django user panel',
        'menu': {
            'top': 'test_project.wp.UserTopMenu',
            'left': 'test_project.wp.UserLeftMenu',
        },
        'dashboard': {
            'breadcrumbs': False,
        },
        'custom_style': STATIC_URL + 'wpadmin/css/themes/ocean.css',
    },
}
