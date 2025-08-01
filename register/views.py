from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Username already exists.')
            user = User.objects.create_user(username=username, password=password)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid input.')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid credentials.')
    return render(request, 'login.html')