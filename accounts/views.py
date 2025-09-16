from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  # добавили logout
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Перенаправьте на главную страницу после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')  # Перенаправление на главную после выхода
