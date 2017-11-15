from django.shortcuts import render



def main(request): 
    context = {} 
    return render(request, 'main/main.html', context) 

def templates(request): 
    return render(request, 'main/templates.html') 

    
