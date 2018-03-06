from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home.html', {})

def scenario(request):
    return render(request, 'scenario.html', {})

def prep_warmer(request):
    return render(request, 'prepwarmer.html', {})

def resuscitation(request):
    return render(request, 'resuscitation.html', {})