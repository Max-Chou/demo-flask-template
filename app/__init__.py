import os
from flask import Flask
from celery import Celery
from config import config
from celeryconfig import celeryconfig
from app.extensions import db, cache, session
from urllib.parse import urljoin

def create_app(config_name="default"):

    # instance
    app = Flask(__name__)

    # config
    app.config.from_object(config[config_name])

    # extensions
    db.init_app(app)
    cache.init_app(app)
    session.init_app(app)
    
    # register
    from app.main.views import main_bp
    app.register_blueprint(main_bp)


    @app.template_global
    def static_url(filepath):
        url = urljoin(app.config['STATIC_URL'], filepath)
        return url


    return app


def create_celery(app=None):

    config_name = os.environ.get("FLASK_CONFIG", "default")
    if app is None:
        app = create_app(config_name)
    
    celery = Celery(__name__)
    celery.config_from_object(celeryconfig[config_name])

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)


    celery.Task = ContextTask
    return celery
