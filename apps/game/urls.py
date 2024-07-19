from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
  path('signup/', signup, name='signup'),
  path('ranking/', ranking, name='ranking'),
  path('list/', list, name='list'),
]