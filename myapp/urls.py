from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='myapp-index'),
    url(r'^appcheck/$', views.appcheck, name='myapp-appcheck'),
]
