from .base import *

DEBUG = False

ALLOWED_HOSTS = ['test.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'test_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
