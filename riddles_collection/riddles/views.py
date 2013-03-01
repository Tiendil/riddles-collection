# coding: utf-8

from django.core.urlresolvers import reverse

from dext.views import BaseResource, handler, validate_argument

from .models import Riddle, Category

def get_riddle_by_id(riddle_id):
    try:
        return Riddle.objects.get(id=riddle_id)
    except Riddle.DoesNotExist:
        return None

def get_category_by_url(category_url):
    try:
        return Category.objects.get(url=category_url)
    except Category.DoesNotExist:
        pass

class RiddlesResource(BaseResource):
    ERROR_TEMPLATE = 'error.html'

    @validate_argument('riddle', get_riddle_by_id, 'riddles', u'Загадка не найдена')
    @validate_argument('page', int, 'riddles', u'Неверная страница')
    @validate_argument('category', get_category_by_url, 'riddles', u'Неверная категория')
    def initialize(self, category=None, riddle=None, page=None):
        super(RiddlesResource, self).initialize()
        self.category = category
        self.riddle = riddle
        self.page = int(page) if page else None

    @handler('#category', '#page', name='', method='get')
    def index(self):

        if self.page is None:
            return self.redirect(reverse('riddles:', args=[self.category.url, 1]))

        RIDDLES_ON_PAGE = 50
        offset = RIDDLES_ON_PAGE * (self.page - 1)

        riddles_query = Riddle.objects.filter(category=self.category).order_by('-created_at', '-id')

        total_count = riddles_query.count()

        riddles = list(riddles_query[offset: offset + RIDDLES_ON_PAGE])

        pages_count = total_count / RIDDLES_ON_PAGE
        if total_count % RIDDLES_ON_PAGE:
            pages_count += 1

        if pages_count < self.page:
            return self.redirect(reverse('riddles:', args=[self.category.url, pages_count]))

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

    @handler('riddle', '#riddle', name='show', method='get')
    def show(self):
        return self.template('riddles/show.html',
                             {'riddle': self.riddle,
                              'category': self.riddle.category,
                              'show_answers': self.request.COOKIES.get('show_answers', 'hide') })
