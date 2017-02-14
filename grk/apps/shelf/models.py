from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre, blank=True)
    website = models.URLField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    decease_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True, null=True)
    description = models.TextField()
    isbn_10 = models.PositiveIntegerField(unique=True)
    isbn_13 = models.PositiveIntegerField(unique=True)
    number_of_pages = models.IntegerField()
    weight = models.IntegerField()
    oclc_number = models.IntegerField()
    physical_dimensions = models.CharField(max_length=100, blank=True, null=True)
    revision = models.IntegerField()
    publishers = models.ForeignKey(Publisher, blank=True, null=True)
    published_date = models.DateField()
    pagination = models.IntegerField(blank=True, null=True)
    lccn = models.IntegerField()
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(Author, related_name='books')

    def __str__(self):
        return self.title


class Language(models.Model):
    language = models.CharField(max_length=100)
    book = models.ForeignKey(Book, related_name='languages')

    def __str__(self):
        return self.language


class Identifier(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    book = models.ForeignKey(Book, related_name='identifiers')

    def __str__(self):
        return self.name


class TableOfContent(models.Model):
    title = models.CharField(max_length=250)
    book = models.ForeignKey(Book, related_name='table_of_contents')

    def __str__(self):
        return self.title
