from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=100)
    hex_value = models.CharField(max_length=7)

# Create your models here.
