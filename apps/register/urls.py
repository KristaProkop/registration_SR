from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^modal_demo/(?P<id>\d+)$', views.display_modal, name='display_modal'),
    url(r'^register/(?P<form_id>\d+)$', views.register, name='register'),
]