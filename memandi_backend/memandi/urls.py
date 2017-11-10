from django.conf.urls import url
from django.conf.urls import include
from rest_framework.authtoken import views as rest_framework_views
from . import views

urlpatterns = [
    url(r'^api/v1/users/$', views.UserList.as_view(), name="user_create_list"),
    url(r'^api/v1/users/(?P<user_id>[0-9]+)/memory$', views.MemoryList.as_view(), name="memory_create_list"),
    url(r'^api/v1/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
