
from django.db import models

from register.models import CustomUser


class Author(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    death_date = models.DateField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    RATE_CHOICES = (
        ('G', 'good'),
        ('M', 'medium'),
        ('B', 'bad'),
        ('NR', 'not rated'),
    )
    book_name = models.CharField(max_length=100)
    pages = models.CharField(max_length=100)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rate = models.CharField(max_length=100, choices=RATE_CHOICES, default='NR')

    def __str__(self):
        return self.book_name
