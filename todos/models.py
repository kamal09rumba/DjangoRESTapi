from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    # text = models.TextField()
    completed = models.BooleanField(null=False,default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title   #this makes djangoadmin page show title inthe list

class SignUp(models.Model):
    email = models.EmailField()
    full_name=models.CharField(max_length=100,blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField