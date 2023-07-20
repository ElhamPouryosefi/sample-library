from newlibrary.models import Book
from django_grpc_framework import generics
from newlibrary.serializers import BookProtoSerializer


class BookService(generics.ModelService):
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer
