# **django��settings����**

#### 1,DEBUG True���²���  False����������

#### 2,ALLOWED_HOST��Ϊ*�����˷���

#### 3,INSTALLED_APPS���app

#### 4,����ģ��templates��DIRS�����os.path,join(BASE_DIR,'ģ��·��')

#### 5,�������ݿ�

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django08',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PWD'),
        'PORT': '3306',
        'HOST': '101.132.145.148',
    }
}

#### 6,�������ԣ�����

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#### 7,���þ�̬�ļ�

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#### 8,���û���

(1)���ݿ���Ϊ����
CACHES = {
    'default': {
         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
         'LOCATION': 'cache_table', #��������ݱ�����
         'TIMEOUT': '60', #���ӳ�ʱ
         'OPTIONS': {
             'MAX_ENTRIES': '300',
         },
         'KEY_PREFIX': 'rock',
        'VERSION': '1',
     }
 }
(2)redis��Ϊ����
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

��hehe��:{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

}

cache_hehe = caches.get['hehe']

#### 9,���ı�����

TINYMCE_DEFAULT_CONFIG = {
        'theme':'advanced',
        'width':800,
        'height':600,
        }

#### 10,�ʼ�����

EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.163.com'  # ����� 163 �ĳ� smtp.163.com

EMAIL_PORT = 465  # smtp�Ķ˿� ���ܸ�

EMAIL_HOST_USER = "17625904460@163.com"  # �˺�

EMAIL_HOST_PASSWORD = "zd010803"  # ��Ȩ��

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Ĭ���ʼ��ķ�����

#### 11,logging��־����

ADMINS = (
    ('zhangding', '17625904460@163.com'),
    ('zd','1574070307@qq.com')
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER
LOGGING = {
    #�汾
    'version': 1,
    #�Ƿ񸲸�֮ǰ����־
    'disable_existing_loggers': False,
    # ���ڿ�����־��Ϣ�����������ʽ
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'easy':{
          'format':'%(asctime)s|%(funcName)s|%(message)s'
        }
    },
    #��������Ҫ��debug��true/false
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true':{
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },


    'handlers': {
        # 'null': {
        #     'level': 'DEBUG',
        #     'class': 'logging.NullHandler',
        # },
        #һ�����ϴ��뱨���ʼ���ʾ
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log", 'debug.log'),  # �ļ�·��
            'maxBytes': 1024 * 1024 * 5, #5M������
            'backupCount': 5,  #����������
            'formatter': 'standard', #�����õĸ�ʽ
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    #�����ĸ�ȫ��Ϊloggers�����
    'loggers': {
        'django': {
            'handlers': ['console','debug'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True, #�Ƿ�̳и����log��Ϣ
        },
        # ���ڲ��� ALLOWED_HOSTS �е����󲻷��ͱ����ʼ�
        'django.security.DisallowedHost': {
            'handlers': ['debug'],
            'propagate': False,
        },
    }
    


