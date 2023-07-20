from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
