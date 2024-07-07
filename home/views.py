from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
from pro.celery import *
from home.tasks import *

from celery.result import *
# Create your views here.

# def index(request):
#     ans = add.delay(10,20)
#     print(ans)
#     ans2 = sub.delay(20,10)
#     print(ans)
#     return HttpResponse("Om Namah Sivay")

def index(request):
    ans = add.apply_async(args = [10,20])
    print(ans)
    return render(request,'home.html',{'ans':ans})

def task_status(reuqest,task_id):
    ans = AsyncResult(task_id)
    return render(reuqest,'result.html', {'ans':ans})