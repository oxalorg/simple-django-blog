from django.conf.urls import url
from .views import archive, article

urlpatterns = [
    url(r'^$', archive, name='archive'), url(r'(?P<slug>[a-zA-Z_0-9\-]*)',
                                             article,
                                             name='article')
]
