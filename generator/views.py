from django.shortcuts import render
from django.http import HttpResponse

import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters=list("abcdefghijklmnopqrstuvwxyz")
    the_password = ""
    length=int(request.GET.get("length"))

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    else:
        pass

    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    else:
        pass

    if request.GET.get("special"):
        characters.extend(list("!#$%^&*()"))
    else:
        pass

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {"password":the_password})

def about(request):
    return render(request, 'generator/about.html')
