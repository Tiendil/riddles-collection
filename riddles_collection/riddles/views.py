# -*- coding: utf-8 -*-
from django_next.views.resources import BaseResource, handler

from .models import Riddle, Category

class RiddlesResource(BaseResource):

    def __init__(self, request, category_url=None, page=None, *args, **kwargs):
        self.category_url = category_url
        self.page = int(page) if page else None
        super(RiddlesResource, self).__init__(request, *args, **kwargs)

    @property
    def category(self):
        if not hasattr(self, '_category'):
            self._category = None
            try:
                self._category = Category.objects.get(url=self.category_url)
            except Category.DoesNotExist:
                pass
                
        return self._category

    @handler('#category_url', '#page', '', method='get')
    def index(self):

        RIDDLES_ON_PAGE = 50
        offset = RIDDLES_ON_PAGE * (self.page - 1)

        riddles_query = Riddle.objects.filter(category=self.category).order_by('-created_at', '-id')

        total_count = riddles_query.count()

        riddles = list(riddles_query[offset: offset + RIDDLES_ON_PAGE])

        pages_count = total_count / RIDDLES_ON_PAGE 
        if total_count % RIDDLES_ON_PAGE:
            pages_count += 1
        
        return self.template('riddles/index.html',
                             {'riddles': riddles,
                              'offset': offset,
                              'page_number': self.page,
                              'pages_count': pages_count,
                              'category': self.category,
                              'RIDDLES_ON_PAGE': RIDDLES_ON_PAGE,
                              'riddles_from': (self.page - 1) * RIDDLES_ON_PAGE + 1,
                              'riddles_to': (self.page - 1) * RIDDLES_ON_PAGE + len(riddles),
                              'total_count': total_count} )
