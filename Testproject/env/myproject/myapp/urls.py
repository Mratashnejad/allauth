
from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'artic'
urlpatterns = [
    url(r'^$', views.app_list, name="list"),
    url(r'^(?P<slug>[\w-]+)/$', views.details, name="detail"),
    # url(r'^(?P<slug>[\w-]+)/$', views.details, name=""), 
]
