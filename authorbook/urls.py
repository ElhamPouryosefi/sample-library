from django.urls import path

from authorbook.views import AddBook, AddBook2, EditBook, EditBook2

urlpatterns = [
    path('addbook/', AddBook.as_view()),
    path('addbook2/', AddBook2.as_view()),
    path('editbook/<int:book_id>/', EditBook.as_view()),
    path('editbook2/', EditBook2.as_view()),
]
