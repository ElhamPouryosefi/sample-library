from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, AuthorSerializer

from .models import Book


@api_view(['GET'])
def get_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book_serializer = BookSerializer(book)
    return Response(book_serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_book(request):
    book = Book.objects.create(
        booke_name=request.POST['book_name'],
        author=request.POST['author'],
        pages=request.POST['pages'],
        rate=request.POST['rate']
    )
    return Response({"message": "new book added successfully", 'book': {
        "book_name": book.book_name,
        "author": book.author,
        "pages": book.pages,
        "rate": book.rate
    }
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book:
        book = request.POST(instance=book)
        book.save()
        return Response({'message': 'book has been updated'})
    return Response({'message': 'book not found!'})


"""
@api_view(['POST'])
def update_book(self, request, book_id, instance):
    book = get_object_or_404(Book, id=book_id)
    
    self.book_name = request.POST(instance)
    self.author = request.POST(instance)
    self.pages = request.POST(instance)
    self.rate = request.POST(instance)
    self.save()
    return Response({'message': 'book has been updated'})
"""

"""
api_view(['POST'])
def update_book(self, instance, request):
    book = get_object_or_404(Book, id=book_id)
    if book:
        instance.book_name = request.POST(book_name=instance.book_name)
        instance.author = request.POST(book_name=instance.author)
        instance.pages = request.POST(book_name=instance.pages)
        instance.rate = request.POST(book_name=instance.rate)
        instance.save()
        return Response({'message': 'book has been updated'})
    return Response({'message': 'book not found!'})
"""


@api_view(['DELETE'])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book:
        book.delete()
        return Response({'message': 'book is deleted'})
    return Response({'message': 'book not found'})
