from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Импортируйте ваши views здесь
from blog.views import FirstPageView, TextPageView, BlogListView, BlogDetailView, SearchView
from tags.views import all_products, drinks_products, meal_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', FirstPageView.as_view(), name='first_page'),
    path('text_page/', TextPageView.as_view(), name='text_page'),
    path('', BlogListView.as_view(), name='blog_list'), # Это корневая страница вашего сайта
    path('blog_list/<int:id>/', BlogDetailView.as_view(), name='blog_detail'),
    path('todo/', include('todo.urls')),
    path('users/', include('users.urls')),
    path('captcha/', include('captcha.urls')),
    path('search/', SearchView.as_view(), name='search'),
    path('all_products/', all_products, name='all_products'),
    path('drinks_products/', drinks_products, name='drinks_products'),
    path('meal_products/', meal_products, name='meal_products'),
    path('cineboard/', include('cineboard.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)