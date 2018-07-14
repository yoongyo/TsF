from django.conf.urls import url
from . import views




urlpatterns =[
    url(r'^$', views.main, name='main'),
    url(r'^local/$', views.local_list, name="local_list"),
    url(r'^local/(?P<City>\w+)/$', views.local_detail, name="local_detail"),
    url(r'^local/(?P<City>\w+)/(?P<pk>\d+)/$', views.local_detail_form, name='local_detail_form'),
    url(r'^new/$', views.post_new, name="post_new")
]


