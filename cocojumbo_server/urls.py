from django.conf.urls import url
from cocojumbo_server import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^cameras/$', views.camera_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
]