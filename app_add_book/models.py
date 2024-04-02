from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField()
    file_text = models.FileField()
    file_img = models.FileField()
    price = models.IntegerField()
    genre = models.CharField(max_length=40)
    release_date = models.DateTimeField()
    # def __str__(self):
    #     return self.name,self.id


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    is_author = models.BooleanField(default=False)
    # created_book = models.ManyToManyField(Book)
   # my_book = models.ManyToManyField(Book)
