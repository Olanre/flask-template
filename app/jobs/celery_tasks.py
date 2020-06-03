from celery import Celery

#uses rabbitmq be default
# Create the app and set the broker location (RabbitMQ)
app = Celery('app',
             backend='rpc://',
             broker='pyamqp://guest@localhost//')

app.task_acks_late = True
app.worker_prefetch_multiplier = 1

@app.task
def add(a, b):
    return a + b

@app.task
def subtract(a, b):
    return a - b