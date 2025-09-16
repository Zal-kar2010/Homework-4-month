from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")),
    path("basket/", include("basket.urls")),
    path('accounts/', include('accounts.urls')),  # ссылки на ваше приложение accounts
    path('captcha/', include('captcha.urls')), 
]