import os
import redis

BASEDIR = os.path.abspath(os.path.dirname(__file__))

class Config():

    SECRET_KEY = os.environ.get('SECRET_KEY', 'ca5f7c3ae9ee4aa49a61f5445830f7c3')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'data-dev.sqlite')
    CACHE_TYPE = 'redis'
    REDIS_URL = "redis://localhost"

    # amazon S3
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', "")

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # static files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

    # public files
    PUBLIC_UPLOAD_LOCATION = 'upload'
    UPLOAD_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_UPLOAD_LOCATION}/'

    # private files
    PRIVATE_UPLOAD_LOCATION = 'prviate'


class DockerConfig(DevelopmentConfig):
    DEBUG = False

    POSTGRES_DB = os.environ.get("POSTGRES_DB")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI = f"postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}:5432/{POSTGRES_DB}"


    CACHE_TYPE = 'memcached'
    CACHE_MEMCACHED_SERVERS = ("memcached:11211",)

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis("redis")

    # amazon S3
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', "")
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', "")
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', "")

    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # static files
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'

    # public files
    PUBLIC_UPLOAD_LOCATION = 'upload'
    UPLOAD_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_UPLOAD_LOCATION}/'

    # private files
    PRIVATE_UPLOAD_LOCATION = 'prviate'


class HerokuConfig(Config):


    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # memcachier
    CACHE_TYPE = 'saslmemcached'
    CACHE_MEMCACHED_SERVERS = os.environ.get("MEMCACHIER_SERVERS", "").split(',')
    CACHE_MEMCACHED_USERNAME = os.environ.get('MEMCACHIER_USERNAME')
    CACHE_MEMCACHED_PASSWORD = os.environ.get('MEMCACHIER_PASSWORD')

    # redis
    REDIS_URL = os.environ.get("REDIS_URL")

    # rabbitmq
    AMQP_URL = os.environ.get("CLOUDAMQP_URL")


config = {
    "development": DevelopmentConfig,
    "heroku": HerokuConfig,
    "docker": DockerConfig,

    "default": DevelopmentConfig,
}