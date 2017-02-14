from django.contrib import admin

from .models import Category, Author, Book, Tag, Publisher, Identifiers, TableOfContent

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Publisher)
admin.site.register(Identifiers)
admin.site.register(TableOfContent)
# Register your models here.
