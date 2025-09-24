from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models, forms
from django.views import generic


class RegisterView(generic.View):
    def get(self, request):
        form = forms.CustomRegisterForm()
        return render(request, 'users/register.html',{'form': form})
    
    def post(self, request):
        form = forms.CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/register.html',{'form': form})



class AuthLoginView(generic.View):
    def get(self, request):
        form = forms.AuthenticationForm()
        return render(request, 'users/login.html', {'form':form})
    def post(self, request):
        form = forms.LoginWithCaptchaForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users:user_list')
        return render(request, 'users/login.html', {'form':form})



class UserListView(LoginRequiredMixin, generic.ListView):
    model = models.CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'user_list'



class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('users:login')

        



