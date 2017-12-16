from edition.models import Sort, Edition

NUM_ITEMS_PER_PAGE = 5

SORT = Sort.objects.filter(disabled=False)
EDITION = Edition.objects.filter(disabled=False)


# Constants available for templates
def showConstants(request):
    context = {
        'SORT':SORT, 
        'EDITION':EDITION

}
    return context
