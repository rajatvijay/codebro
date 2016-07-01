from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'new/$', views.paste_create, name='paste_create'),
    url(r'list/$', views.paste_list, name='paste_list'),
    url(r'(?P<slug>\w+)/detail/$', views.paste_detail, name='paste_detail'),
    url(r'(?P<slug>\w+)/raw/$', views.paste_raw, name='paste_raw'),

]
