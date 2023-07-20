from newlibrary.models import Book
from django_grpc_framework import proto_serializers
import newlibrary_pb2


class BookProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Book
        proto_class = newlibrary_pb2.Book
        fields = ['id', 'book_name', 'author', 'pages']
