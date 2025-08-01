from django.shortcuts import render, HttpResponse

def home(requests):
    return render(requests, 'index.html')