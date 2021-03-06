# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
        #url(r'^posts/(?P<post_class>[a-zA-Z]+)/(?P<post_type>[a-zA-Z0-9]+)/$', views.get_posts_list, name = 'posts_list'),
        url(r'^post/first/$', views.get_post, name='post_first'),
        url(r'^post/list/$', views.get_posts_list, name='memo_list'),
        url(r'^archives/$', views.archives, name='archives'),
        url(r'^archive', views.archive_get, name='archive_get'),
        url(r'^dir_list/$', views.dir_list),
        url(r'^post/content/(?P<filename>.*)/$', views.one_markdown, name='post_content'),
        ]  
        
