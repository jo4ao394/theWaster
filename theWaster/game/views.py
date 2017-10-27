from django.shortcuts import render


def game(request): 
    context = {} 
    return render(request, 'game/game.html', context) 
