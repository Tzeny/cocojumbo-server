from django.db import models


class Camera(models.Model):
    name = models.TextField()


class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    cameras = models.ManyToManyField(Camera)


class Alert(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.TextField()
