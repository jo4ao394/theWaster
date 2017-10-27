from django.conf.urls import url

from edition import views


urlpatterns = [
    url(r'^$', views.edition, name='edition'),
]