from django.shortcuts import render

from edition.models import Sort, Edition


def main(request): 
    context = {} 
    return render(request, 'main/main.html', context) 


def templates(request): 
    return render(request, 'main/templates.html') 

