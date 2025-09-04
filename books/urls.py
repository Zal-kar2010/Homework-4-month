from django.urls import path
from . import views

urlpatterns = [
    path('ru/', views.book_ru, name='book_ru'),
    path('en/', views.book_en, name='book_en'),
    path('usa/', views.book_usa, name='book_usa'),
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
]