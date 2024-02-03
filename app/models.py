from django.db import models

# Create your models here.

# tasks/models.py
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=50)
    assigned_to = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# chat/models.py
class Message(models.Model):
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

