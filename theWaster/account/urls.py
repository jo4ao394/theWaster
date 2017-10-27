from django.conf.urls import url

from account import views


urlpatterns = [
    url(r'^$', views.account, name='account'),
]
