from django.contrib import admin

# Register your models here.

# tasks/admin.py
from django.contrib import admin
from .models import Task

admin.site.register(Task)

# chat/admin.py
from django.contrib import admin
from .models import Message

admin.site.register(Message)
