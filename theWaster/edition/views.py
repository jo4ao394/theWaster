from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from edition.forms import EditionForm
from edition.models import Edition


def edition(request): 
    context = {} 
    return render(request, 'edition/edition.html', context) 


def editionCreate(request): 
    template = 'edition/editionCreate.html' 
    if request.method == 'GET': 
        return render(request, template, {'editionForm':EditionForm()}) 
    # POST 
    editionForm = EditionForm(request.POST) 
    if not editionForm.is_valid(): 
        return render(request, template, {'editionForm':EditionForm}) 
    editionForm.save() 
    messages.success(request, '版喻已新增\o/') 
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
