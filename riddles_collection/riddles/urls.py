
from django_next.views.dispatcher import resource_patterns

from .views import RiddlesResource

urlpatterns = resource_patterns(RiddlesResource)



