from django.urls import path #include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # ← эта строка должна быть
    path('ru/', views.book_ru, name='book_ru'),
    path('en/', views.book_en, name='book_en'),
    path('usa/', views.book_usa, name='book_usa'),
    path('detail/<int:book_id>/', views.book_detail, name='book_detail'),
    path('tours/', views.tour_list, name='tour_list'),
    path('tours/register/<int:tour_id>/', views.register_for_tour, name='register_for_tour'),
    path('tours/success/', views.registration_success, name='registration_success'),
]
def home(request):
    return render(request, 'books/home.html')