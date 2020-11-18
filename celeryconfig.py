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


celeryconfig = {
    "docker": DockerConfig,

    "default": Config
}