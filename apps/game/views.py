from django.shortcuts import render, redirect
from apps.game.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Game, User
from django.db.models import Q

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


# def create_fight(request):


def game_list(request):
    games = Game.objects.filter(
        Q(attackerId=request.user.id) | Q(defenderId=request.user.id)
    ).order_by("-id")
    attacks, defends = [], []
    for game in games:
        attacks.append(str(game.attackerId))
        defends.append(str(game.defenderId))
    game_list_name = zip(games, attacks, defends)
    context = {"user": request.user, "game_list_name": game_list_name}
    return render(request, "list.html", context=context)
