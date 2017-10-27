from django.shortcuts import render


def account(request): 
    context = {} 
    return render(request, 'account/account.html', context) 
