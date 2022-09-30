from django.db import models

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name    = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=20)
