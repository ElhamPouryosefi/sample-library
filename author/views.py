from anotherbook.serializers import AuthorSerializer
from anotherbook.models import Author
from rest_framework import generics


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UpdateAuthor(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class DestroyAuthor(generics.DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CreateAuthor(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
