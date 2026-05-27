from celery import Celery

celery_app = Celery("modular_tasks", broker="amqp://guest@localhost//5672", backend="redis://localhost//6379")

celery_app.autodiscover_tasks()