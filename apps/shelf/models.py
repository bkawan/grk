from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=250)


class Author(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    decease_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Categories'

class Tag(models.Model):
    title = models.CharField(max_length=250)


class Book(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True, null=True)
    description = models.TextField()
    isbn = models.PositiveIntegerField(unique=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    author = models.ForeignKey(Author, related_name='books')

