from rest_framework import viewsets, mixins, status
from rest_framework.decorators import detail_route
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import CategorySerializer, AuthorSerializer, BookSerializer, TagSerializer, PublisherSerializer, \
    IdentifierSerializer, LanguageSerializer, TableOfContentSerializer
from .models import Category, Author, Book, Tag, Publisher, Identifier, TableOfContent, Language


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @detail_route()
    def books(self, request, pk):
        try:
            author = get_object_or_404(Author, pk=pk)
            books = author.books.all()
            return Response(BookSerializer(books, many=True).data, status=status.HTTP_200_OK)
        except:
            return Response({'error': True}, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PublisherViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class IdentifierViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Identifier.objects.all()
    serializer_class = IdentifierSerializer


class TableOfContentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TableOfContent.objects.all()
    serializer_class = TableOfContentSerializer


class LanguageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
