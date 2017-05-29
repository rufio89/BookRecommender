from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lookup/$', views.lookup, name='lookup'),
    # ex: /polls/5/
    url(r'^detail/(?P<isbn>[A-z0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<isbn>[A-z0-9]+)/results/$', views.results, name='results'),


]