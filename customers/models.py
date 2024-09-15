from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    industy = models.CharField(max_length=100)
