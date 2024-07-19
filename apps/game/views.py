from django.shortcuts import render, redirect
from apps.game.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Game, User
from django.db.models import Q
import random

# Create your views here.


def signup(request):  # 회원가입
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # auth.login(request, user)
            return redirect("game:main")
        else:
            return render(request, "signup.html", {"form": form})
    else:  # get메소드
        form = SignupForm()  # 회원가입 폼 전달
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
        form = AuthenticationForm()  # 장고에서 지원하는 로그인 폼?
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


def start_attack(request):
    user = request.user  # 로그인한 유저
    if request.method == "GET":
        opponents = User.objects.exclude(id=user.id)  # 로그인한 유저 제외 모든 유저
        available_cards = []
        num = 5
        while num > 0:
            number = random.randint(1, 10)
            if number not in available_cards:
                available_cards.append(number)
                num -= 1
            else:
                continue
        available_cards.sort()
        context = {"opponents": opponents, "available_cards": available_cards}
        return render(request, "attack1.html", context)
    if request.method == "POST":
        Game.objects.create(
            status=0,  # 게임 진행중
            attackerId=user,
            attackerCard=request.POST["search_card"],
            defenderId=User.objects.get(id=request.POST["search_opponent"]),
            defenderCard=0,  # 게임 진행중이라 아직 선택 X
            winner=0,
        )
        return redirect("game:game_list")


def counter(request, pk):
    game = Game.objects.get(id=pk)  # 반격할 게임 정보 가져옴
    if request.method == "GET":
        available_cards = []
        num = 5
        while num > 0:
            number = random.randint(1, 10)
            if number not in available_cards:
                available_cards.append(number)
                num -= 1
            else:
                continue
        available_cards.sort()
        context = {"available_cards": available_cards}
        return render(request, "attack2.html", context)
    if request.method == "POST":
        game.defenderCard = int(request.POST["search_card"])  # 반격자가 낸 카드
        game.status = 1  # 게임 상태: 게임 종료
        num = random.randint(0, 1)
        if num == 0:  # 작을 때 이김
            game.rule_value = 0
            if game.attackerCard > game.defenderCard:  # 공격자가 더 크면
                game.winner = int(game.defenderId.id)  # 승리자는 반격자
                game.attackerId.score -= game.attackerCard
                game.defenderId.score += game.defenderCard
            elif game.attackerCard < game.defenderCard:  # 반격자가 더 크면
                game.winner = int(game.attackerId.id)  # 승리자는 공격자
                game.attackerId.score += game.attackerCard
                game.defenderId.score -= game.defenderCard
            else:
                game.winner = -1
        if num == 1:  # 클 때 이김
            game.rule_value = 1
            if game.attackerCard > game.defenderCard:  # 공격자가 더 크면
                game.winner = int(game.attackerId.id)  # 승리자는 공격자
                game.attackerId.score += game.attackerCard
                game.defenderId.score -= game.defenderCard
            elif game.attackerCard < game.defenderCard:  # 반격자가 더 크면
                game.winner = int(game.defenderId.id)  # 승리자는 반격자
                game.attackerId.score -= game.attackerCard
                game.defenderId.score += game.defenderCard
            else:
                game.winner = -1
        game.save()  # 게임정보 저장
        game.attackerId.save()  # 공격자 점수 정보 저장
        game.defenderId.save()  # 반격자 점수 정보 저장
        return redirect(f"/gameInfo/{pk}")  # 게임 결과 화면으로 이동


def gameInfo(request, pk):
    game = Game.objects.get(id=pk)  # 반격할 게임 정보 가져옴
    if game.status == 1:
        attacker = User.objects.get(id=game.attackerId.id)
        defender = User.objects.get(id=game.defenderId.id)
        user = request.user
        context = {"game": game, "attacker": attacker, "defender": defender, "user": user, "game_rule":game.rule[game.rule_value]}
    else:
        attacker = User.objects.get(id=game.attackerId.id)
        defender = User.objects.get(id=game.defenderId.id)
        user = request.user
        context = {"game": game, "attacker": attacker, "defender": defender, "user": user}
    
    return render(request, "gameInfo.html", context)

def ranking(request):
    users = User.objects.all().order_by('-score')[:3]
    context = {"users":users}
    return render(request, "ranking.html", context)

def cancel(request, pk):
    Game.objects.get(id=pk).delete()
    return redirect("game:game_list")