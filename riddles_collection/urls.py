from django.conf.urls.defaults import patterns, url, include, handler404, handler500

from django.contrib import admin
from django.conf import settings

from django_next import jinja2 as jinja2_next
from django_next.views.views import template_renderer

admin.autodiscover()
jinja2_next.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       url(r'^$', template_renderer('index.html'), name='index'),
                       (r'^riddles/', include('riddles.urls', namespace='riddles') ),
)

if settings.DEBUG:
    urlpatterns +=  patterns('',
                             url(r'^less/', include('django_next.less.urls') ) )
