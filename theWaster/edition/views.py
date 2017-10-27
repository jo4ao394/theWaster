from django.shortcuts import render

def edition(request): 
    context = {} 
    return render(request, 'edition/edition.html', context) 
