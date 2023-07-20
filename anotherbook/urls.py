from django.urls import path

from .views import RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

urlpatterns = [
    path('get/<int:book_id>/', RetrieveAPIView.as_view()),
    path('add/', CreateAPIView.as_view()),
    path('update/', UpdateAPIView.as_view()),
    path('delete/', DestroyAPIView.as_view()),
    path('list/', ListAPIView.as_view()),
]
