from app import create_celery


celery = create_celery()

@celery.task
def long_task():
    return "a long task"
