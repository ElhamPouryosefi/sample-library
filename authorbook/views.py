from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from anotherbook.models import Book
from .permissions import IsAuthorUser, IsAuthorOfBook, IsAuthorOfBook2
from anotherbook.serializers import AddBookRequestSerializer, BookSerializer
from .serializers import UpdateSerializer, UpdateBookSerializer


class AddBook(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        book_request_serializer = AddBookRequestSerializer(data=request.data)
        book_request_serializer.is_valid(raise_exception=True)
        book_serializer = BookSerializer(data=book_request_serializer.data)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response({'message': 'Book added successfully!'})


class AddBook2(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorUser]

    def post(self, request):
        request_data = {"author": request.user.id, **request.data}
        book_request_serializer = AddBookRequestSerializer(data=request_data)
        book_request_serializer.is_valid(raise_exception=True)

        book_serializer = BookSerializer(data=book_request_serializer.data)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response({'message': 'Book added successfully!'})


class EditBook(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOfBook]

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book_serializer = BookSerializer(instance=book, data=request.data, partial=True)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response({'message': 'book has been updated'})


class EditBook2(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthorOfBook2]

    def post(self, request, book_id):
        obj = Book.objects.get(id=book_id)
        request_serializer = UpdateSerializer(instance=obj, data=request.data, partial=True)
        request_serializer.is_valid(raise_exception=True)
        book_serializer = UpdateBookSerializer(request_serializer)
        book_serializer.is_valid()
        book_serializer.save()
        return Response({'message': 'book has been updated'})


