from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)              # название книги
    author = models.CharField(max_length=100)             # автор
    description = models.TextField()                      # описание
    published_date = models.DateField()                   # дата публикации
    pages = models.IntegerField()                         # количество страниц
    language = models.CharField(max_length=50)            # язык книги
    genre = models.CharField(max_length=50)               # жанр
    isbn = models.CharField(max_length=20, unique=True)   # ISBN
    price = models.DecimalField(max_digits=8, decimal_places=2)  # цена
    created_at = models.DateTimeField(auto_now_add=True)  # дата добавления

    def __str__(self):
        return self.title
