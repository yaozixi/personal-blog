from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^archive', archive, name='archive'),
    url(r'^comment', comment_order, name='comment'),
]
