from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse("<h1>ESTA E A PAGINA INDEX OU PAGINA HOME.</h1>")


def contato(request):
    return HttpResponse("<h1>ESTA E A PAGINA DE CONTATOS</h1>")
