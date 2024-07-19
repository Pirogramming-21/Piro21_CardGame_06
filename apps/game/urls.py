from django.urls import path
from .views import *

app_name = "game"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("", main, name="main"),
    path("start", start_attack, name="start"),
    path("counter/<int:pk>", counter, name="counter"),
    path("counter/<int:pk>", counter, name="counter"),
    path("gameInfo/<int:pk>", gameInfo, name="gameInfo"),
]
