from django.urls import path
from .views import *

app_name = "game"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("", main, name="main"),
    path("game_list/", game_list, name="game_list"),
]
