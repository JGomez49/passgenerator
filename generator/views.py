from django.shortcuts import render
# from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def passwords(request):
    chars = list('abcdefghijklmnoprstuvwxyz')
    new_pass = ''

    x = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('number'):
        chars.extend(list('0123456789'))

    if request.GET.get('special'):
        chars.extend(list('~!@#$%^&*()_+=-?<>'))

    for x in range(x):
        new_pass = new_pass + random.choice(chars)

    return render(request, 'generator/passwords.html', {'password': new_pass})