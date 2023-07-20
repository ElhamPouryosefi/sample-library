from django_grpc_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AddBookRequestSerializer

from .models import Book


class RetrieveAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        book_serializer = BookSerializer(instance=book)
        data = book_serializer.data
        return Response({'Book': data})


class CreateAPIView(APIView):
    def post(self, request):
        book_request_serializer = AddBookRequestSerializer(data=request.data)
        book_request_serializer.is_valid(raise_exception=True)
        book_serializer = BookSerializer(data=book_request_serializer.data)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response({'message': 'Book added successfully!'})


class UpdateAPIView(APIView):
    def post(self, request, book_id):
        book = get_object_or_404(Book, book_id)
        book_serializer = BookSerializer(instance=book, data=request.data, partial=True)
        data = book_serializer.data
        data.save()
        return Response({'message': 'book has been updated'})


class DestroyAPIView(APIView):
    def delete(self, request, book_id):
        book = get_object_or_404(Book, book_id)
        book_serializer = BookSerializer(instance=book)
        data = book_serializer.data
        data.delete()
        return Response({'message': 'book is deleted'})


class ListAPIView(APIView):
    def get(self, request):
        book = Book.objects.all()
        book_serializer = BookSerializer(book, many=True)
        return Response({'message': book_serializer.data})


class BookViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Book.objects.all()
        serializer = Book(queryset, many=True)
        return Response(serializer.data)

