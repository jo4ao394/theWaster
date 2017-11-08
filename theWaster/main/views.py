from django.shortcuts import render

from edition.models import Sort, Edition


def main(request): 
    context = {} 
    return render(request, 'main/main.html', context) 

def templates(request): 
    sorts = Sort.objects.all()
    editions = Edition.objects.all()
    context = {'sorts':sorts, 'editions':editions}
    return render(request, 'main/templates.html', context) 

    
