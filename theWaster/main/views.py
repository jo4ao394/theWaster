from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from main.constants import NUM_ITEMS_PER_PAGE

def main(request): 
    context = {} 
    return render(request, 'main/main.html', context) 


def templates(request): 
    return render(request, 'main/templates.html') 


def pagination(request, queryset, numItemsPerPage=NUM_ITEMS_PER_PAGE):   
    paginator = Paginator(queryset, numItemsPerPage)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    
    fullPath = request.get_full_path()
    if fullPath.find('?') < 0:    # No search terms: add a question mark so that 'page' may be appended
        fullPath += '?'
    else:    # There are search terms
        index = fullPath.find('page')
        if index < 0:        # No 'page': add an '&' so that 'page' may be appended
            fullPath += '&'
        else:                # There is 'page': remove 'page' info
            fullPath = fullPath[:index]
            
    return {'queryset':queryset, 'paginator':paginator, 'fullPath':fullPath}