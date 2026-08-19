from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('Home') 

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')

# Create your views here.
