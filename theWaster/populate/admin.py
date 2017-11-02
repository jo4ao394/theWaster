from populate import base
from django.contrib.auth.models import User


def populate(): 
    print('Creating admin account ... ', end='')
    User.objects.all().delete()
    User.objects.create_superuser(username='admin', password='admin', email=None)
    User.objects.create_superuser(username='ailan12345', password='ailan12345', email=None)
    User.objects.create_superuser(username='ballfish', password='ballfish', email=None)
    User.objects.create_superuser(username='shunmao', password='shunmao', email=None)

    print('done')


if __name__ == '__main__':
    populate()