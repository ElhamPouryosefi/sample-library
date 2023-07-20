from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
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
    pages = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rate = models.CharField(max_length=100, choices=RATE_CHOICES, default='NR')

    def __str__(self):
        return self.book_name
