from django.db import models
from datetime import datetime
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100000)
    date_created = models.DateTimeField(datetime.now, blank=True)

