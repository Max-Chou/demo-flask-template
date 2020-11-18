web: gunicorn manage:app
worker: celery -A app.tasks worker -B --loglevel=info