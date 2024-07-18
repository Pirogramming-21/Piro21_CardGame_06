from django.urls import path
from .views import *

app_name = "game"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("", main, name="main"),
]
