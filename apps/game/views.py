from django.shortcuts import render, redirect
from .models import *

def signup(request):
    return render(request, 'signup.html')


def ranking(request):
    return render(request,'ranking.html')

def list(request):
    return render(request,'list.html')