from rest_framework import serializers
from book.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name', 'birth_date', 'death_date')
