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
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # 启用严格模式
            'charset': 'utf8mb4',  # 设置字符集
        },
    }
}
