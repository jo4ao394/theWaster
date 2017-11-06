from populate import base 
from django.contrib.auth.models import User

from edition.models import Sort, Edition



titles = ['AAAAA', 'HSLSCMCJ'] 
sorts = ['校園', '日常', '遊戲'] 



def populate(): 
    print('EEEEEEEEEEEEE ... ', end='') 
    Sort.objects.all().delete() 
    Edition.objects.all().delete() 
    for sortname in sorts: 
        sort = Sort() 
        sort.sort = sortname 
        sort.save() 
        for title in titles: 
            for i in range(1,3): 
                edition = Edition() 
                edition.sort = sort
                edition.edition = title+str(i)
                #edition.user = User.objects.get(username='admin')
                edition.save() 
    print('done') 

if __name__ == '__main__': 
    populate()