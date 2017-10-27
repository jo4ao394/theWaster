from django.conf.urls import url

from game import views


urlpatterns = [
    url(r'^$', views.game, name='game'),
]
