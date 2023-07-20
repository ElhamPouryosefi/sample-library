from django.urls import path
from .views import BookList, UpdateBook, DestroyBook, CreateBook
urlpatterns = [
    #path('create_book/', create_book),
    path('list/', BookList.as_view()),
    path('update/<int:pk>/', UpdateBook.as_view()),
    path('delete/<int:pk>/', DestroyBook.as_view()),
    path('create/<int:pk>/', CreateBook.as_view()),
]
