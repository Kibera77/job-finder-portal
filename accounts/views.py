from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import UserRegisterForm


# Create your views here.


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the users
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login_user.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'accounts/logout_user.html')
