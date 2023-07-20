from rest_framework import serializers

from register.models import CustomUser
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'birth_date',)


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Book
        fields = ('book_name', 'author', 'pages', 'rate')


class AddBookRequestSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    author = serializers.IntegerField()
    pages = serializers.IntegerField()
