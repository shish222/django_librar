from django.db import models


# Create your models here.
class author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)


class book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    auth = models.ManyToManyField(author)
    file = models.FileField()
