from django.urls import path
from . import views

app_name = 'cineboard'

urlpatterns = [
    # User authentication and management paths
    path('register_cine/', views.RegisterView.as_view(), name='register_cine'),
    path('login_cine/', views.AuthLoginView.as_view(), name='login_cine'),
    path('logout_cine/', views.AuthLogoutView.as_view(), name='logout_cine'),

    # Film listing and creation paths
    path('all_films/', views.AllFilmsListView.as_view(), name='all_films'),
    path('create_film/', views.CreateFilmView.as_view(), name='create_film'),
    
    # Film detail, update, and delete paths
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'), # New path for film details
    path('film/<int:pk>/add_comment/', views.AddCommentView.as_view(), name='add_comment'), # New path to add comments
    
    # Existing update and delete paths - consider changing 'id' to 'pk' for consistency
    path('all_films/<int:id>/update/', views.UpdateFilmView.as_view(), name='update_film'), # Renamed for clarity
    path('all_films/<int:id>/delete/', views.DeleteFilmView.as_view(), name='delete_film'), # Renamed for clarity
]