from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_app/', include('test_app.urls')),

    path('about', views.aboutpage),
    path('', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()