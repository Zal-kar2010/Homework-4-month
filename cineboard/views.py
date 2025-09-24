from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Avg
from django.http import HttpResponse

from . import models, forms


# CBV для создания фильма
class CreateFilmView(generic.CreateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/createFilm.html'
    success_url = '/all_films/'


# CBV для редактирования фильма
class UpdateFilmView(generic.UpdateView):
  model = models.Films
  form_class = forms.FilmsForm
  template_name = 'cineboard/updateFilm.html'
  success_url = '/all_films/'

  def get_object(self, *args, **kwargs):
    film_id = self.kwargs.get('id')
    return get_object_or_404(models.Films, id=film_id)
  
  def form_valid(self, form):
    print(form.cleaned_data)
    return super(UpdateFilmView, self).form_valid(form=form)


# CBV для удаления фильма
class DeleteFilmView(generic.DeleteView):
  template_name = 'cineboard/confirm_delete_film.html'
  success_url = '/all_films/'

  def get_object(self, *args, **kwargs):
    film_id = self.kwargs.get('id')
    return get_object_or_404(models.Films, id=film_id)


# CBV для регистрации
class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, template_name='cineboard/register_cine.html', context={'form':form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_cine/')
        return render(request, template_name='cineboard/register_cine.html', context={'form': form})
    

# CBV для входа
class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'cineboard/login_cine.html', {'form':form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cineboard:all_films')
        return render(request, 'cineboard/login_cine.html', {'form':form})


# CBV для списка фильмов с поиском, фильтрацией и сортировкой
class AllFilmsListView(LoginRequiredMixin, generic.ListView):
    model = models.Films
    template_name = 'cineboard/tv_list.html'
    context_object_name = 'tv_lst'

    def get_queryset(self):
        # Сортировка по среднему рейтингу
        queryset = super().get_queryset().annotate(avg_rating=Avg('rating__marks')).order_by('-avg_rating')

        # Поиск по названию или описанию
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        
        # Фильтрация по жанру (тегу)
        tag = self.request.GET.get('tag')
        if tag:
            queryset = queryset.filter(tags__name__icontains=tag)
            
        return queryset

# CBV для выхода
class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cineboard:login_cine')

# Новый CBV для детальной страницы фильма
class FilmDetailView(generic.DetailView):
    model = models.Films
    template_name = 'cineboard/film_detail.html'
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.CommentForm()
        return context

# Новый CBV для добавления комментария
class AddCommentView(LoginRequiredMixin, generic.View):
    def post(self, request, pk):
        film = get_object_or_404(models.Films, pk=pk)
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.author = request.user
            comment.save()
        return redirect('cineboard:film_detail', pk=pk)
    