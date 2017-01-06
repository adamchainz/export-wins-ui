"""
Django settings for ui project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", False))

# As the app is running behind a host-based router supplied by Heroku or other
# PaaS, we can open ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    # django
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    # third party
    "django_extensions",
    "raven.contrib.django.raven_compat",

    # project apps
    "ui",
    "users",
    "wins",
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'ui.middleware.SSLRedirectMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "alice.middleware.AliceMiddleware",
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "ui.context_processors.handy",
            ],
        },
    },
]

WSGI_APPLICATION = 'ui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# We're still using a database on the UI because outright removing it causes
# problems since so many packages require contenttypes which requires a db. The
# important part though is that the database is effectively static data,
# created at deploy time.  There's no session or user info in there, so there's
# nothing to worry about on that front.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'


# URLs for access points on the data server
DATA_SERVER = os.getenv("DATA_SERVER")
WINS_AP = "{}/wins/".format(DATA_SERVER)
WIN_DETAILS_AP = "{}/details/".format(DATA_SERVER)
LIMITED_WINS_AP = "{}/limited-wins/".format(DATA_SERVER)
CONFIRMATIONS_AP = "{}/confirmations/".format(DATA_SERVER)
BREAKDOWNS_AP = "{}/breakdowns/".format(DATA_SERVER)
ADVISORS_AP = "{}/advisors/".format(DATA_SERVER)
NOTIFICATIONS_AP = "{}/notifications/".format(DATA_SERVER)
LOGIN_AP = "{}/auth/login/".format(DATA_SERVER)
LOGOUT_AP = "{}/auth/logout/".format(DATA_SERVER)
IS_LOGGED_IN_AP = "{}/auth/is-logged-in/".format(DATA_SERVER)
CSV_AP = "{}/csv/".format(DATA_SERVER)
ADD_USER_AP = "{}/admin/add-user/".format(DATA_SERVER)
NEW_PASSWORD_AP = "{}/admin/new-password/".format(DATA_SERVER)
SEND_CUSTOMER_EMAIL_AP = "{}/admin/send-customer-email/".format(DATA_SERVER)
SEND_ADMIN_CUSTOMER_EMAIL_AP = "{}/admin/send-admin-customer-email/".format(DATA_SERVER)
CHANGE_CUSTOMER_EMAIL_AP = "{}/admin/change-customer-email/".format(DATA_SERVER)
SOFT_DELETE_AP = "{}/admin/soft-delete/".format(DATA_SERVER)


# For UI server should match UI_SECRET in data server, for admin server should
# match ADMIN_SECRET in data server.
UI_SECRET = os.getenv("UI_SECRET")


# for JWT
COOKIE_SECRET = os.getenv("COOKIE_SECRET")


# Mail stuffs
FEEDBACK_ADDRESS = os.getenv("FEEDBACK_ADDRESS")
SENDING_ADDRESS = os.getenv("SENDING_ADDRESS")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = bool(os.getenv("EMAIL_USE_TLS"))
EMAIL_USE_SSL = bool(os.getenv("EMAIL_USE_SSL"))
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT")) if os.getenv("EMAIL_TIMEOUT") else None
EMAIL_SSL_KEYFILE = os.getenv("EMAIL_SSL_KEYFILE")
EMAIL_SSL_CERTFILE = os.getenv("EMAIL_SSL_CERTFILE")
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")  # The default is just fine


# Google Analytics
ANALYTICS_ID = os.getenv("ANALYTICS_ID")


# how long you can edit a win
EDIT_TIMEOUT_DAYS = int(os.getenv('EDIT_TIMEOUT_DAYS', 120))


# Sentry
RAVEN_CONFIG = {
    "dsn": os.getenv("SENTRY_DSN"),
}


# Security stuff
SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
if DEBUG:
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False


STAGING = os.getenv("STAGING")
