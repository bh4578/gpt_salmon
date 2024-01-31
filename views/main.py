from django.shortcuts import render


def index(request):
    return render(request, "index/main.html")


def salmon(request):
    return render(request, "index/salmon.html")