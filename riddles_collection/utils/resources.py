# coding: utf-8


from dext.views import BaseResource

class Resource(BaseResource):

    ERROR_TEMPLATE = 'error.html'

    def __init__(self, request, *args, **kwargs):
        super(Resource, self).__init__(request, *args, **kwargs)
        self.user = self.request.user
