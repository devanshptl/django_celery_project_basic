from celery import shared_task
from time import sleep

@shared_task(namw = "custome")
def sub(x,y):
    sleep(10)
    return x-y

@shared_task
def happy(id):
    print("Happy Birthday",id)
    return id