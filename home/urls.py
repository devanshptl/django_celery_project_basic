from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('result/<str:task_id>',views.task_status, name = "result"),
]
