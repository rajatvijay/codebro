from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new/$', views.paste_create, name='post_create'),
    url(r'list/$', views.paste_list, name='post_list'),
    url(r'detail/(?P<slug>\w+)/$', views.paste_detail, name='paste_detail'),
    url(r'formatter/(?P<slug>\w+)/$', views.paste_formatter, name='paste_formatter'),
]
