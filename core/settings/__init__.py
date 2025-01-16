from decouple import config

# 获取环境变量 DJANGO_ENV，默认值为 local
DJANGO_ENV = config('DJANGO_ENV', default='local')

print(DJANGO_ENV)
if DJANGO_ENV == 'local':
    from .local import *
elif DJANGO_ENV == 'test':
    from .test import *
elif DJANGO_ENV == 'prod':
    from .prod import *
else:
    raise ValueError(f"Unknown DJANGO_ENV: {DJANGO_ENV}")
