from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title' : "Добавить статью", 'url_name' : 'add_page'},
    {'title': "Обратная связь", 'url_name' : 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': "Анджелина Джоли", 'content':'Биография Анджелины Джоли', 'is_published':True},
    {'id': 2, 'title': "Марго Робби", 'content':'Биография Марго Робби', 'is_published' : False},
    {'id': 3, 'title': "Джулия Робертс", 'content':'Биография Джулии Робертс', 'is_published':True},
]

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'women/index.html', context=data)


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2025:
        # raise Http404()
        # return redirect('/', permanent=True)
        # return redirect(index, permanent=True)
        # наиболее правильно использовать имена путей
        redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архив по годам:</h1><p>{year}</p>")


def about(request):
    data = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'women/about.html', context=data)

def page_not_found(request, exception):
    return HttpResponse("<h1>Страница не найдена</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная свзяь")

def login(request):
    return HttpResponse("Авторизация")