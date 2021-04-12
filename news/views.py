from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h3>Hello World !</h3>")