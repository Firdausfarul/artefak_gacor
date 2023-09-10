from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    img = models.TextField()
    emoji = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    continent = models.CharField(max_length=255)
    price = models.IntegerField()
