from rest_framework import serializers

from .models import Category, Author, Book, Tag, Publisher, Identifier, TableOfContent, Language


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class IdentifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identifier
        fields = '__all__'


class TableOfContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableOfContent
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    languages = LanguageSerializer(many=True)
    identifiers = IdentifierSerializer(many=True)
    table_of_contents = TableOfContentSerializer(many=True)

    class Meta:
        model = Book
        depth = 1
        fields = '__all__'
