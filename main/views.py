from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Выбери устройство</h2>")


def about(request):
    return render(request, 'main/about.html')


def kdtn(request):
    return render(request, 'main/kdtn.html')


def uspd(request):
    return HttpResponse("<h2>Страница про УСПД</h2>")


def tou(request):
    return HttpResponse("<h2>Страница про ТОУ</h2>")
