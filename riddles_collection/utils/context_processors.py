
from riddles.models import Category

def categories(request):
    return {'categories': list(Category.objects.all().order_by('name'))}
