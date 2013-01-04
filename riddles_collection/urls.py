# coding: utf-8

from django.conf.urls.defaults import patterns, url, include

from django.contrib import admin
from django.conf import settings as project_settings

from dext import jinja2 as jinja2_next
from dext.views import create_handler_view

from portal.views import PortalResource


admin.autodiscover()
jinja2_next.autodiscover()

urlpatterns = patterns('',
                       (r'^admin/', include(admin.site.urls)),
                       (r'^riddles/', include('riddles.urls', namespace='riddles') ),
                       (r'^', include('portal.urls', namespace='portal') ),
)

if project_settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += patterns('',
                            url(r'^%s' % project_settings.LESS_CSS_URL[1:], include('dext.less.urls') )
                            )
    urlpatterns += static(project_settings.DCONT_URL, document_root=project_settings.DCONT_DIR)
    urlpatterns += static(project_settings.STATIC_URL, document_root=project_settings.STATIC_DIR)


handler404 = create_handler_view(PortalResource, 'handler404')
handler500 = create_handler_view(PortalResource, 'handler500')
