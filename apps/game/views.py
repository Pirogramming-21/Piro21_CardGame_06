from django.shortcuts import render, redirect
from apps.game.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Game, User

# Create your views here.


def signup(request): #회원가입
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():# 이부분 설명 필요
            user = form.save()
            auth.login(request, user)#atth가 무엇
            return redirect("game:main")
        else:
            return render(request, "signup.html", {"form": form})
    else: #get메소드
        form = SignupForm() #회원가입 폼 전달
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
        form = AuthenticationForm()#장고에서 지원하는 로그인 폼?
        return render(request, "login.html", {"form": form})


def main(request):
    return render(request, "main.html")
