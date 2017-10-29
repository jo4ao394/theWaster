from django.conf.urls import url

from edition import views


urlpatterns = [
    url(r'^$', views.edition, name='edition'),
    
    url(r'^editionCreate/$', views.editionCreate, name='editionCreate'), 
    
    url(r'^editionUpdate/(?P<editionId>[0-9]+)/$', views.editionUpdate, name='editionUpdate'),
]