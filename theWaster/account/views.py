from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



def account(request): 
    context = {}
    return render(request, 'account/account.html', context) 

def login(request):
    template = 'account/login.html'
    if request.method == 'GET':
        return render(request, template, {'nextURL':request.GET.get('next')})
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:    # Server-side validation
        messages.error(request, '請填資料')
        return render(request, template)
    user = authenticate(username=username, password=password)
    if not user:    # authentication fails
        messages.error(request, '登入失敗')
        return render(request, template)
    if not user.is_active:
        messages.error(request, '帳號已停用')
        return render(request, template)
    # login success
    auth_login(request, user)
    nextURL = request.POST.get('nextURL')
    if nextURL:
        return redirect(nextURL)
    messages.success(request, '登入成功')
    return redirect('main:templates')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '歡迎再度光臨')
    return redirect('main:main') 