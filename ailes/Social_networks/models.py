from django.db import models
from functools import reduce

class MainInfo(models.Model):
    login = models.BinaryField()
    password = models.BinaryField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)





