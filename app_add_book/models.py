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
    release_date = models.DateField()
    # def __str__(self):
    #     return self.name,self.id


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.FileField()
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120)
    is_author = models.BooleanField(default=False)
    created_book = models.ManyToManyField(Book, related_name="created_book")
    my_book = models.ManyToManyField(Book, related_name="my_book")
    balance = models.IntegerField(default=10)
    bio = models.CharField(max_length=200)
