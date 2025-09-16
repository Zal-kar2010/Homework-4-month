from django.contrib import admin
from .models import Book, Review, HorseTour, TourRegistration

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'language', 'get_review_count']  # ← УБРАТЬ published_date
    list_filter = ['language', 'author']  # ← УБРАТЬ published_date
    search_fields = ['title', 'author']
    
    def get_review_count(self, obj):
        return obj.reviews.count()
    get_review_count.short_description = 'Отзывов'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['book__title', 'user__username']

@admin.register(HorseTour)
class HorseTourAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'price', 'available_slots']
    list_filter = ['duration']
    search_fields = ['name', 'description']

@admin.register(TourRegistration)
class TourRegistrationAdmin(admin.ModelAdmin):
    list_display = ['user', 'tour', 'participants', 'registration_date']
    list_filter = ['tour', 'registration_date']
    search_fields = ['user__username', 'tour__name']