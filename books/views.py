from .serializers import BookSerializer
from book.models import Book
from rest_framework import generics


class BookList1(generics.ListCreateAPIView):
    def get_serializer_class(self):
        return BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateBook(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DestroyBook(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBook(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
