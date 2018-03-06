from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^scenario', views.scenario, name='scenario'),
    url(r'^prepwarmer', views.prep_warmer, name='prepwarmer'),
    url(r'^resuscitation', views.resuscitation, name='resuscitation'),
]