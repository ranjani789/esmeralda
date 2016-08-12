"""
Django settings for esmeralda project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wt_jifbzt+^8ayklo(4v@_g)n-l(zpbbv2yp!ya2=b=)c3vt68'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'esmeralda',
    'jquery',
    'pipeline',
    'stream',
    'twitter_bootstrap',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'esmeralda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'esmeralda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

## django-pipeline configuration
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
PIPELINE = {
    'STYLESHEETS': {
        'bootstrap': {
            'source_filenames': (
                'esmeralda/less/esmeralda.less',
            ),
            'output_filename': 'css/b.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'jquery': {
            'source_filenames': (
	        'js/jquery.js',
            ),
            'output_filename': 'js/j.js',
	},
        'bootstrap': {
            'source_filenames': (
                'twitter_bootstrap/js/transition.js',
                'twitter_bootstrap/js/modal.js',
                'twitter_bootstrap/js/dropdown.js',
                'twitter_bootstrap/js/scrollspy.js',
                'twitter_bootstrap/js/tab.js',
                'twitter_bootstrap/js/tooltip.js',
                'twitter_bootstrap/js/popover.js',
                'twitter_bootstrap/js/alert.js',
                'twitter_bootstrap/js/button.js',
                'twitter_bootstrap/js/collapse.js',
                'twitter_bootstrap/js/carousel.js',
                'twitter_bootstrap/js/affix.js',
            ),
            'output_filename': 'js/b.js',
	}
    },
}


# Configure LESS to search in certain projects static folders
esmeralda_less = os.path.join(BASE_DIR, 'esmeralda', 'static', 'esmeralda', 'less')
import twitter_bootstrap
bootstrap_less = os.path.join(os.path.dirname(twitter_bootstrap.__file__), 'static', 'twitter_bootstrap', 'less')

PIPELINE['LESS_ARGUMENTS'] = u'--include-path={}'.format(os.pathsep.join([bootstrap_less, esmeralda_less]))
PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['COMPILERS'] = (
  'pipeline.compilers.less.LessCompiler',
)

