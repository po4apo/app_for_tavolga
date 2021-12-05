import datetime

from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    photo = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    # todo: Добавить поле comment:text и completed:bool

    REQUIRED_FIELDS = ['created_on', 'photo']



# Не для детей

class Event(models.Model):
    name = models.CharField(max_length=255)


class Nomination(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Document(models.Model):
    document_name = models.CharField(max_length=255)
    document_json = models.JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    nomination = models.ForeignKey(Nomination, on_delete=models.CASCADE)
    # updated_on = models.DateTimeField(auto_now_add=True)
