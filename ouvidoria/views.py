from django.shortcuts import render
from django.http import HttpResponse


def helloWorld(request):
    return HttpResponse('Hello World')

def form_manifestacao(request):
    return render(request, 'main/form_manifestacao.html')

def yourName(request, name):
    return render(request, 'main/yourName.html', {'name': name})