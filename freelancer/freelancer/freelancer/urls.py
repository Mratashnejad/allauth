from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home_page , name='portfolio'),
    url(r'^about/$', views.about_Page , name="about"),
    url(r'^contact/$',views.contact_Page , name="contact"),
    url(r'^account/', include('account.urls')),
    url(r'^blackjack/$', views.blackjack_page, name="blackjack"),
    url(r'^roulette/$', views.roulette_page, name="roulette"),
    url(r'^poker/$', views.poker_page , name="poker"),
]

urlpatterns += staticfiles_urlpatterns()