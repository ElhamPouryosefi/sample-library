from django.urls import path
from .views import AuthorList, CreateAuthor, UpdateAuthor, DestroyAuthor

urlpatterns = [
    path('get/', AuthorList.as_view()),
    path('update/<int:pk>/', UpdateAuthor.as_view()),
    path('delete/<int:pk>/', DestroyAuthor.as_view()),
    path('create/', CreateAuthor.as_view()),
]
