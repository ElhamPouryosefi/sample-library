from rest_framework import serializers
from anotherbook.models import Book
from register.models import CustomUser


class UpdateBookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Book
        fields = ('book_name', 'author', 'pages', 'rate')


class UpdateSerializer(serializers.Serializer):
    book_name = serializers.CharField()
    author = serializers.IntegerField()
    pages = serializers.IntegerField()
    book_id = serializers.IntegerField()
