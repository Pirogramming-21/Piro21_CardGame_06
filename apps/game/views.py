from django.shortcuts import render, redirect
from apps.game.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Game, User

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # auth.login(request, user)
            return redirect("game:main")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = SignupForm()
        return render(request, "signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect("game:main")
        else:
            return render(request, "login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def logout(request):
    auth.logout(request)
    return redirect("game:main")


def main(request):
    return render(request, "main.html")
