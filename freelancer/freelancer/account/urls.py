from django.urls import path, include
from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
    url(r'^$', views.account),
    url(r'^signup/$', views.signup, name='Signup'),
    url(r'^login/$',views.login , name='Login'),
]