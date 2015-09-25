from django.conf.urls.defaults import *
from webapp import urls

urlpatterns = patterns('',
    (r'', include(urls)),
)
