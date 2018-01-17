from django.db import models


class Question(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)  
