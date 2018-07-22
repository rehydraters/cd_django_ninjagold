from django.conf.urls import url, include
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^process_money/(?P<location>\w+)$', views.process_money),
  ]