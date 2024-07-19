from django.shortcuts import render

# Create your views here.
def social_login(request):
    return render(request, 'login.html')