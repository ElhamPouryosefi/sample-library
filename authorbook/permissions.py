from rest_framework.permissions import BasePermission


class IsAuthorUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_author is True:
            return True
        else:
            return False


class IsAuthorOfBook(BasePermission):
    def has_permission(self, request, view):
        if request.user == request.GET.get('book_id'):
            return True
        else:
            return False


class IsAuthorOfBook2(BasePermission):
    def has_permission(self, request, obj):
        if request.user == obj:
            return True
        else:
            return False
