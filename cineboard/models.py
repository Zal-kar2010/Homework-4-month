from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, default='Романтика')



class Films(models.Model):
    GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Хорор', 'Хоррор')
    )
    title = models.CharField(max_length=100, default='фильм1')
    description = models.TextField(default='Описание фильма')
    genre = models.CharField(max_length=100, choices=GENRE, default='Фантастика')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    MARKS = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ('4', "4"),
        ('5', '5')
    )
    choice_films = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='rating')
    marks = models.CharField(max_length=100, choices=MARKS, default='3', null=True)


class Comment(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.film.title}'    