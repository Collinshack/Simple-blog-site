from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=100000)
    thumbnail = models.ImageField(upload_to = "images/", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(datetime.now, blank=True)

