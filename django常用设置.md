# **django中settings配置**

#### 1,DEBUG True线下测试  False生产环境跑

#### 2,ALLOWED_HOST改为*所有人访问

#### 3,INSTALLED_APPS添加app

#### 4,配置模板templates在DIRS中添加os.path,join(BASE_DIR,'模板路径')

#### 5,配置数据库

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

#### 6,配置语言，汉化

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#### 7,配置静态文件

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

#### 8,配置缓存

(1)数据库作为缓存
CACHES = {
    'default': {
         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
         'LOCATION': 'cache_table', #缓存的数据表名字
         'TIMEOUT': '60', #连接超时
         'OPTIONS': {
             'MAX_ENTRIES': '300',
         },
         'KEY_PREFIX': 'rock',
        'VERSION': '1',
     }
 }
(2)redis作为缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

“hehe”:{
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }

}

cache_hehe = caches.get['hehe']

#### 9,富文本设置

TINYMCE_DEFAULT_CONFIG = {
        'theme':'advanced',
        'width':800,
        'height':600,
        }

#### 10,邮件设置

EMAIL_USE_SSL = True

EMAIL_HOST = 'smtp.163.com'  # 如果是 163 改成 smtp.163.com

EMAIL_PORT = 465  # smtp的端口 不能改

EMAIL_HOST_USER = "17625904460@163.com"  # 账号

EMAIL_HOST_PASSWORD = "zd010803"  # 授权码

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 默认邮件的发送人

#### 11,logging日志设置

ADMINS = (
    ('zhangding', '17625904460@163.com'),
    ('zd','1574070307@qq.com')
)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SERVER_EMAIL = EMAIL_HOST_USER
LOGGING = {
    #版本
    'version': 1,
    #是否覆盖之前的日志
    'disable_existing_loggers': False,
    # 用于控制日志信息的最终输出格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'easy':{
          'format':'%(asctime)s|%(funcName)s|%(message)s'
        }
    },
    #过滤条件要求debug是true/false
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
        #一旦线上代码报错，邮件提示
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, "log", 'debug.log'),  # 文件路径
            'maxBytes': 1024 * 1024 * 5, #5M的数据
            'backupCount': 5,  #允许几个备份
            'formatter': 'standard', #上面用的格式
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    #上面四个全是为loggers服务的
    'loggers': {
        'django': {
            'handlers': ['console','debug'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.request': {
            'handlers': ['debug', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True, #是否继承父类的log信息
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['debug'],
            'propagate': False,
        },
    }
    


