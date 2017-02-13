from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=250)


class Tag(models.Model):
    title = models.CharField(max_length=250)


class Book(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True, null=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    author = models.ForeignKey(Author, related_name='books')

