from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    language = models.CharField(max_length=20, choices=[
        ('ru', 'Русский'),
        ('en', 'Английский'), 
        ('usa', 'Американский')
    ])
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Отзыв на {self.book.title} от {self.user.username}"

class HorseTour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_slots = models.IntegerField()
    
    def __str__(self):
        return self.name

class TourRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tour_registration')
    tour = models.ForeignKey(HorseTour, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    participants = models.IntegerField(default=1)
    special_requests = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.tour.name}"
    
    