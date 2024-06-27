from django.shortcuts import render

def home(require):
    return render(require, 'testeApp/home.html')
