from django.conf.urls import url

from edition import views


urlpatterns = [
    url(r'^$', views.sortEdition, name='sortEdition'),
    
    url(r'^sortCreate/$', views.sortCreate, name='sortCreate'), 
    url(r'^editionCreate/$', views.editionCreate, name='editionCreate'),
    
    url(r'^sortUpdate/(?P<editionId>[0-9]+)/$', views.sortUpdate, name='sortUpdate'),
    url(r'^editionUpdate/(?P<editionId>[0-9]+)/$', views.editionUpdate, name='editionUpdate'),


    url(r'^article/(?P<articleName>)/$', views.article, name='article'),
]