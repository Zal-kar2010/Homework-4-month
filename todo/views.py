from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic

#CRUD - Create Read Update Delete

#Create

class CreateTodo(generic.CreateView):
  model = models.Todo
  form_class = forms.TodoForm
  template_name = 'create_todo.html'
  success_url = '/todo_list/'


#Read
class ReadTodoView(generic.ListView):
  model = models.Todo
  template_name = 'todo_list.html'
  context_object_name = 'todo'
  ordering = ['-id']


#Update
class UpdateTodoView(generic.UpdateView):
  model = models.Todo
  form_class = forms.TodoForm
  template_name = 'update_todo.html'
  success_url = '/todo_list/'

  def get_object(self, *args, **kwargs):
    todo_id = self.kwargs.get('id')
    return get_object_or_404(models.Todo, id=todo_id)
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super(UpdateTodoView, self).form_valid(form=form)


#Delete
class DeleteTodoView(generic.DeleteView):
  template_name = 'confirm_delete.html'
  success_url = '/todo_list/'

  def get_object(self, *args, **kwargs):
    todo_id = self.kwargs.get('id')
    return get_object_or_404(models.Todo, id=todo_id)

