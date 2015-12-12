from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'webapp.views.index'),
    (r'^mvaultaction/$', 'webapp.views.mvaultaction'),
    (r'^mvaultentry/$', 'webapp.views.mvaultentry'),
)
