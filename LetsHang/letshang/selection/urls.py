from django.conf.urls import url, include
from . import views

urlpatterns = [
    #/selection/
    url(r'^$', views.index, name='index'),

    #/selection/1/ (2 or 3)
    url(r'^(?P<selection_id>[0-9]+)/$', views.choice, name='choice'),
    url(r'^(?P<selection_id>[0-9]+)/match/$', views.choice, name='choice'),
]
