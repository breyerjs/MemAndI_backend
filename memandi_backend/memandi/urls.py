from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/users/$', views.create_user, name="user"),
    url(r'^api/v1/users/(?P<user_id>[0-9]+)/memory$', views.create_memory, name="create_memory")
    ]
