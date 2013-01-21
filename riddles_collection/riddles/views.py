# coding: utf-8

from dext.views import BaseResource, handler

from .models import Riddle, Category

class RiddlesResource(BaseResource):

    def initialize(self, category_url=None, riddle_id=None, page=None):
        super(RiddlesResource, self).initialize()
        self.category_url = category_url
        self.riddle_id = riddle_id
        self.page = int(page) if page else None

    @property
    def category(self):
        if not hasattr(self, '_category'):
            self._category = None
            try:
                self._category = Category.objects.get(url=self.category_url)
            except Category.DoesNotExist:
                pass

        return self._category

    @property
    def riddle(self):
        if not hasattr(self, '_riddle'):
            try:
                self._riddle = Riddle.objects.get(id=self.riddle_id)
            except Riddle.DoesNotExist:
                self._riddle = None
        return self._riddle

    @handler('#category_url', '#page', name='', method='get')
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
                              'show_answers': self.request.COOKIES.get('show_answers', 'hide'),
                              'offset': offset,
                              'page_number': self.page,
                              'pages_count': pages_count,
                              'category': self.category,
                              'RIDDLES_ON_PAGE': RIDDLES_ON_PAGE,
                              'riddles_from': (self.page - 1) * RIDDLES_ON_PAGE + 1,
                              'riddles_to': (self.page - 1) * RIDDLES_ON_PAGE + len(riddles),
                              'total_count': total_count} )

    @handler('riddle', '#riddle_id', name='show', method='get')
    def show(self):
        return self.template('riddles/show.html',
                             {'riddle': self.riddle,
                              'category': self.riddle.category,
                              'show_answers': self.request.COOKIES.get('show_answers', 'hide') })
