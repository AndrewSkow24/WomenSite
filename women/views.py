from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Главная страница")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")