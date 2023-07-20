from django.contrib import admin
from django.urls import path, include
from newlibrary.services import BookService
import newlibrary_pb2_grpc


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('anotherbook/', include('anotherbook.urls')),
    # path('books/', include('books.urls')),
    path('author/', include('author.urls')),
    path('register/', include('register.urls')),
    path('authorbook/', include('authorbook.urls')),
]


def grpc_handlers(server):
    newlibrary_pb2_grpc.add_BookControllerServicer_to_server(BookService.as_servicer(), server)
