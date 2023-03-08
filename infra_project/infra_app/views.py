from django.http import HttpResponse
from django.shortcuts import render

python_basics = (
    "Знакомство с Python",
    "Циклы и ветвления",
    "Функции",
    "Словари и множества",
    "Строки и форматирование",
    "Библиотеки",
    "Протокол HTTP",
    "Сетевые запросы",

)

django_backend = (
    "Базы данных",
    "Python, IDE, venv",
    "Git, Pytest",
    "OOP",
    "Urls, views",
    "Верстка в Django",
    "Шаблоны, теги в Django",
    "Декораторы",
    "Тестирование",
    "Подписки на авторов",
)

api = (
    "API First. Архитектура REST",
    "Ресурсы, эндпоинты, HTTP методы",
    "Исследование запросов",
    "Протокол Auth 2.0",
    "Бот-ассистент",
    "REST API, Проектирование",
    "Сериализаторы",
    "Вьюсеты и роутеры",
    "Regular Expressions",
    "JWT + Djoser",
)

algos = (
    "Линейный поиск",
    "Бинарный поиск",
    "Сложность алгоритма",
    "Структуры данных",
    "Рекурсия и сортировки",
    "Хеш-функции, коллизии",
    "Двоичные деревья",
    "Поисковый индекс",
)

vm = (
    "VirtualBox",
    "SSH",
    "WSGI, NGINX",
    "Gunicorn, systemd",
    "PostgreSQL",
    "Docker",
    "Docker-compose",
    "DockerHub",
    "DevOps",
    "CI и CD",
)


def index(request):
    context = {
        'algos': algos,
        'api': api,
        'django_backend': django_backend,
        'python_basics': python_basics,
        'vm': vm,
    }
    return render(request, 'infra_app/base.html', context)


def second_page(request):
    return HttpResponse('А это вторая страница!')
