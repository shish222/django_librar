from django.db import models


# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    auth = models.ManyToManyField(Admin)
    file = models.FileField()
    price = models.IntegerField()
