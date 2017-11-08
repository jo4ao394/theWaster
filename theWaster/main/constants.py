from edition.models import Sort, Edition


SORT = Sort.objects.all()
EDITION = Edition.objects.all()


# Constants available for templates
def showConstants(request):
    context = {
        'SORT':SORT, 
        'EDITION':EDITION

}
    return context
