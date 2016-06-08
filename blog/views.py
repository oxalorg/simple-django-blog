from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('Hello. You\'re at blog index')


def front(request):
    return render(request, 'blog/front.html')


def about(request):
    return HttpResponse('about page')


def support(request):
    return HttpResponse('support page')
