from django.urls import path
from . import views

urlpatterns = [
  path('todo_list/', views.ReadTodoView.as_view(), name='todo_list'),
  path('create_todo/', views.CreateTodo.as_view(), name="create_todo"),
  path('update_todo/<int:id>/', views.UpdateTodoView.as_view(), name='update_todo'),
  path('delete_todo/<int:id>/', views.DeleteTodoView.as_view(), name='delete_todo'),
]