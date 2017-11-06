from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request

from edition.forms import EditionForm, SortForm
from edition.models import Edition, Sort, Article


def sortEdition(request):
    sorts = Sort.objects.all()
    editions = Edition.objects.all()
    return render(request, 'edition/sortEdition.html',{'sorts':sorts, 'editions':editions}) 




def article(request):
    article = Article.objects.all()
    return render(request, 'edition/article.html', {'article':article}) 

    
def sortCreate(request): 
    template = 'edition/sortCreate.html' 
    if request.method == 'GET': 
        return render(request, template, {'sortForm':SortForm()}) 
    # POST 
    sortForm = SortForm(request.POST) 
    if not sortForm.is_valid(): 
        return render(request, template, {'sortForm':SortForm}) 
    sortForm.save() 
    messages.success(request, '類別已新增\o/') 
    return redirect('edition:sort') 


def editionCreate(request): 
    template = 'edition/editionCreate.html' 
    if request.method == 'GET': 
        return render(request, template, {'editionForm':EditionForm()}) 
    # POST 
    editionForm = EditionForm(request.POST) 
    if not editionForm.is_valid(): 
        return render(request, template, {'editionForm':EditionForm}) 
    editionForm.save() 
    messages.success(request, '版域已新增\o/') 
    return redirect('edition:edition') 


def sortUpdate(request,sortId): 
    template = 'edition/sortUpdate.html' 
    sort = get_object_or_404(Sort,id=sortId) 
    #POST
    sortForm = SortForm(request.POST, instance=sort) 
    if not sortForm.is_valid(): 
        return render(request, template, {'sortForm':sortForm}) 
    sortForm.save() 
    messages.success(request, '修改成功')  
    return redirect('edition:edition') 


def editionUpdate(request,editionId): 
    template = 'edition/editionUpdate.html' 
    edition = get_object_or_404(Edition,id=editionId) 
    #POST
    editionForm = EditionForm(request.POST, instance=edition) 
    if not editionForm.is_valid(): 
        return render(request, template, {'editionForm':editionForm}) 
    editionForm.save() 
    messages.success(request, '修改成功')  
    return redirect('edition:edition') 



