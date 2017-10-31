from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'users/create^$', views.create_user, name='create_user'),
]
