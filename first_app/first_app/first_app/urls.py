from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$' , views.home_page, name = 'homepage'),

]

urlpatterns += staticfiles_urlpatterns()