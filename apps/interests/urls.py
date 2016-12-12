from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
    url(r'^interests/(?P<id>\d+)$', views.interests)
 ]
