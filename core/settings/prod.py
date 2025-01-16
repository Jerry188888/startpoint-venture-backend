from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prod_db',
        'USER': 'prod_user',
        'PASSWORD': 'prod_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# 生产环境安全设置
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
