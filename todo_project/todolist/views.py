from django.http import HttpResponse
from django.shortcuts import render

def index(request, *args, **kwargs):
    return HttpResponse("ok")