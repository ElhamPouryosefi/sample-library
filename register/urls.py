from django.urls import path
from .views import login, Register, Register2, LogoutAPIView, ChangePassword

urlpatterns = [
    path('login/', login),
    path('logout/', LogoutAPIView.as_view()),
    path('create/', Register.as_view()),
    path('create2/', Register2.as_view()),
    path('password/', ChangePassword.as_view()),
]
