# coding: utf-8

from django.core.urlresolvers import reverse

from dext.views import handler

from utils.resources import Resource


class PortalResource(Resource):

    # render error taken by exception middleware
    def error(self, msg=None):
        return self.template('error.html', {'msg': msg})

    # render error taken by exception middleware
    def handler403(self, msg=None):
        return self.template('403.html', {'msg': msg})

    @handler('', method='get')
    def index(self):
        from riddles.models import Category

        try:
            category = Category.objects.all().order_by('name')[0]
            return self.redirect(reverse('riddles:', args=[category.url, 1]))
        except:
            pass
        return self.template('portal/index.html', {})

    @handler('404', method='get')
    def handler404(self):
        return self.template('portal/404.html', status_code=404)

    @handler('500', method='get')
    def handler500(self):
        return self.template('portal/500.html')
