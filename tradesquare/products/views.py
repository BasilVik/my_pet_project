from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком товаров
def products_list(request):
    return HttpResponse('Список товаров')


# Страница с информацией об одном товаре;
# view-функция принимает параметр pk из path()
def products_detail(request, pk):
    return HttpResponse(f'Товар номер {pk}')