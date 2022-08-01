from django.db import models
from django.contrib.auth import models as auth_models

'''
documentation fields: https://docs.djangoproject.com/en/4.0/ref/models/fields/
'''


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)


class Articles(models.Model):
    title = models.CharField(max_length=200)
    intro_article = models.TextField(blank=False)
    article = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
