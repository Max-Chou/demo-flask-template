import os

class Config():
    broker_url = 'redis://localhost:5672'
    result_backend = 'redis://localhost:6379'

    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    imports = ('app.tasks', )


class DockerConfig(Config):
    broker_url = 'amqp://rabbitmq:5672'
    result_backend = 'redis://redis:6379'


class HerokuConfig(Config):
    broker_url = os.environ.get("CLOUDAMQP_URL")
    result_backend = os.environ.get("REDIS_URL")


celeryconfig = {
    "docker": DockerConfig,
    "heroku": HerokuConfig,

    "default": Config
}